# -*- mode: python -*-

block_cipher = None


a = Analysis(['__main__.py'],
             pathex=[r'{SRC_PATH}'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[r'{BUILD_PATH}'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=True,
             win_private_assemblies=True,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='{APP_NAME}',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
			   [
					('icon.ico', 'icon.ico', 'DATA'),
			   ],
			   Tree('static\\', prefix='static\\'),
			   Tree('templates\\', prefix='templates\\'),
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='__main__')
