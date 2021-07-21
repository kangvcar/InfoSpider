# Build exe and nsis installer

import contextlib
import hashlib
import os
import importlib.util
import subprocess
import shutil


# -- CHANGE
PROJECT_FOLDER_NAME = 'wendy'
MAKENSIS_PATH = '"C:\\Program Files (x86)\\NSIS\\makensis.exe"'
# --

BUILD_PATH = os.getcwd()
ROOT_PATH = os.path.dirname(BUILD_PATH)
SRC_PATH = os.path.join(ROOT_PATH, PROJECT_FOLDER_NAME)


@contextlib.contextmanager
def cd(new_path):
    cwd = os.getcwd()
    os.chdir(new_path)
    try:
        yield
    finally:
        os.chdir(cwd)


if __name__ == '__main__':

    print("BUILD_PATH {}".format(BUILD_PATH))
    print("ROOT_PATH {}".format(ROOT_PATH))
    print("SRC_PATH {}".format(SRC_PATH))

    print(
        "#################\n"
        "# Load __info__ #\n"
        "#################\n")

    info_path = os.path.join(SRC_PATH, '__info__.py')
    spec = importlib.util.spec_from_file_location("module.name", info_path)
    info = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(info)

    APP_NAME = info.APP_NAME
    APP_NAME_NO_SPACE = info.APP_NAME_NO_SPACE
    APP_VERSION = info.APP_VERSION
    APP_DESC = info.APP_DESCRIPTION
    COMPANY_NAME = info.COMPANY_NAME
    WEBSITE = info.WEBSITE

    print(APP_NAME)
    print(APP_NAME_NO_SPACE)
    print(APP_VERSION)

    print(
        "#############\n"
        "# copy spec #\n"
        "#############\n")

    with open('build.spec', 'r', encoding='utf-8') as f:
        spec_text = f.read()

    spec_text = spec_text.format(SRC_PATH=SRC_PATH, APP_NAME=APP_NAME, BUILD_PATH=BUILD_PATH)

    SPEC_PATH = os.path.join(SRC_PATH, 'build.spec')
    print(SPEC_PATH)

    with open(SPEC_PATH, 'w', encoding='UTF-8') as f:
        f.write(spec_text)

    print(
        "###################\n"
        "# run pyinstaller #\n"
        "###################\n")

    original_cwd = os.getcwd()
    os.chdir(SRC_PATH)

    try:
        cmd = "pyinstaller --clean -F build.spec"
        print(cmd)
        subprocess.check_output(cmd, shell=True)
    except:
        raise
    finally:
        os.remove(SPEC_PATH)
        if os.path.isdir('build'):
            shutil.rmtree('build')
        os.chdir(original_cwd)

    print(
        "#############\n"
        "# copy dist #\n"
        "#############\n")

    path = os.path.join(SRC_PATH, 'dist', '__main__')
    folder = "{}_v{}".format(PROJECT_FOLDER_NAME, APP_VERSION)
    LATEST_DIST_PATH = os.path.join(BUILD_PATH, 'dist', folder)
    LATEST_DIST_SRC = os.path.join(LATEST_DIST_PATH, PROJECT_FOLDER_NAME)
    print(LATEST_DIST_PATH)
    print(LATEST_DIST_SRC)
    shutil.move(path, LATEST_DIST_SRC)

    print(
        "##############\n"
        "# write nsis #\n"
        "##############\n")

    # -- Gather files for installer

    install_text = ""
    uninstall_text = ""
    for root, dirs, files in os.walk(LATEST_DIST_SRC):
        try:
            root = root.split(LATEST_DIST_SRC + "\\")[1].strip()
        except IndexError:
            root = ""

        line = 'CreateDirectory "$INSTDIR\\{}\\"\n'.format(root)
        install_text += line
        delete_dir = 'RMDir "$INSTDIR\\{}\\"\n'.format(root)
        line = 'SetOutPath "$INSTDIR\\{}\\"\n'.format(root)
        install_text += line
        for f in files:
            if root:
                line = 'file "{}\\{}"\n'.format(root, f)
                delete_line = 'Delete "$INSTDIR\\{}\\{}"\n'.format(root, f)
            else:
                line = 'file "{}"\n'.format(f)
                delete_line = 'Delete "$INSTDIR\\{}"\n'.format(f)
            install_text += line
            uninstall_text += delete_line
        uninstall_text += delete_dir
    uninstall_text += 'RMDir "$INSTDIR\\"'
    # --

    nsis_path = os.path.join(BUILD_PATH, 'installer.nsi')
    with open(nsis_path, 'r', encoding='utf-8') as f:
        nsis_text = f.read()

    brand = "{} v{} - {}".format(APP_NAME, APP_VERSION, WEBSITE)
    ico_big_path = os.path.join(BUILD_PATH, 'icon.ico')
    header_path = os.path.join(BUILD_PATH, 'header.bmp')
    license_path = os.path.join(BUILD_PATH, 'license.txt')
    exe_name = "{}.exe".format(APP_NAME)
    INSTALLER_OUT_NAME = "Install-{}-v{}.exe".format(APP_NAME_NO_SPACE, APP_VERSION)
    nsis_text = nsis_text.format(
        NAME=APP_NAME,
        BRAND=brand,
        NAMENOSPACE=APP_NAME_NO_SPACE,
        DESCRIPTION=APP_DESC,
        ICOPATH=ico_big_path,
        HEADERPATH=header_path,
        LICENSEPATH=license_path,
        EXENAME=exe_name,
        INSTALLFILES=install_text,
        DELETEFILES=uninstall_text,
        INSTALLEROUTNAME=INSTALLER_OUT_NAME,
        VERSION=APP_VERSION,
        COMPANY_NAME=COMPANY_NAME,
        WEBSITE=WEBSITE,
    )

    nsi_path = os.path.join(LATEST_DIST_SRC, 'installer.nsi')
    print(nsi_path)
    with open(nsi_path, 'w', encoding='utf-8') as f:
        f.write(nsis_text)

    print(
        "###################\n"
        "# build installer #\n"
        "###################\n")

    build_command = "{} /V3 ./installer.nsi".format(MAKENSIS_PATH)
    with cd(LATEST_DIST_SRC):
        subprocess.check_output(build_command, shell=True)
        os.remove('installer.nsi')
        shutil.move("./{}".format(INSTALLER_OUT_NAME), LATEST_DIST_PATH)

    INSTALLER_EXE_PATH = os.path.join(LATEST_DIST_PATH, INSTALLER_OUT_NAME)
    print(INSTALLER_EXE_PATH)

    print(
        "################################\n"
        "# generate hashes of installer #\n"
        "################################\n")

    hash_md5 = hashlib.md5()
    hash_sha1 = hashlib.sha1()
    hash_sha256 = hashlib.sha256()
    hash_sha512 = hashlib.sha512()
    with open(INSTALLER_EXE_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(6144), b""):
            hash_md5.update(chunk)
            hash_sha1.update(chunk)
            hash_sha256.update(chunk)
            hash_sha512.update(chunk)

    hash_file_name = "hashes-{}-v{}.txt".format(APP_NAME_NO_SPACE, APP_VERSION)
    hash_path = os.path.join(LATEST_DIST_PATH, hash_file_name)
    with open(hash_path, 'w', encoding='utf-8') as f:
        f.write("MD5:{}\n".format(hash_md5.hexdigest()))
        f.write("SHA1:{}\n".format(hash_sha1.hexdigest()))
        f.write("SHA256:{}\n".format(hash_sha256.hexdigest()))
        f.write("SHA512:{}\n".format(hash_sha512.hexdigest()))

    print(
        "!!!!!!!!!!!!\n"
        "! FINISHED !\n"
        "!!!!!!!!!!!!\n")