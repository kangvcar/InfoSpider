;NSIS Modern User Interface
;Basic Example Script
;Written by Joost Verburg

;------------------------
;Setting vars
!define APPNAME "{NAME}"
!define COMPANYNAME "{COMPANY_NAME}"
!define DESCRIPTION "{DESCRIPTION}"
!define WEBSITE "{WEBSITE}"
Var StartMenuFolder
BrandingText "{BRAND}"



;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

  !include "FileFunc.nsh"

;--------------------------------
;General

  ;Name and file
  Name "{NAMENOSPACE}"
  OutFile "{INSTALLEROUTNAME}"
  

  ;Default installation folder
  InstallDir "$PROGRAMFILES\${{COMPANYNAME}}\${{APPNAME}}"
  
  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\${{COMPANYNAME}}\${{APPNAME}}" ""

  ;Request application privileges for Windows Vista
  RequestExecutionLevel admin

  
  
;--------------------------------
;Interface Configuration

  !define MUI_ICON "{ICOPATH}"
  !define MUI_HEADERIMAGE
  !define MUI_HEADERIMAGE_BITMAP "{HEADERPATH}" ; optional
  !define MUI_ABORTWARNING

;--------------------------------

;Pages

  !insertmacro MUI_PAGE_LICENSE "{LICENSEPATH}"
  !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  ;Start Menu Folder Page Configuration
  !define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU" 
  !define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\${{COMPANYNAME}}\${{APPNAME}}"
  !define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${{APPNAME}}"
  !insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder
  !insertmacro MUI_PAGE_INSTFILES
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  
  
  # These indented statements modify settings for MUI_PAGE_FINISH
	!define MUI_FINISHPAGE_NOAUTOCLOSE
	!define MUI_FINISHPAGE_RUN
	!define MUI_FINISHPAGE_RUN_NOTCHECKED
	!define MUI_FINISHPAGE_RUN_TEXT "Start {NAME}"
	!define MUI_FINISHPAGE_RUN_FUNCTION "LaunchLink"
	!insertmacro MUI_PAGE_FINISH
	
	Function LaunchLink
	  ExecShell "" "$INSTDIR\{EXENAME}"
	FunctionEnd
  
  
;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

Section "${{APPNAME}}" SecDummy

  SectionIn RO ;Make it read-only
  SetOutPath "$INSTDIR"
  
  ;ADD YOUR OWN FILES HERE...

{INSTALLFILES}



  SetOutPath "$INSTDIR"
  
  ;Store installation folder
  WriteRegStr HKCU "Software\${{COMPANYNAME}}\${{APPNAME}}" "" $INSTDIR

  ;Register Add Remove
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${{APPNAME}}" \
                 "DisplayName" "${{APPNAME}}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${{APPNAME}}" \
                 "UninstallString" "$\"$INSTDIR\Uninstall {EXENAME}$\""
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${{APPNAME}}" \
                 "DisplayIcon" "$\"$INSTDIR\icon.ico$\""
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${{APPNAME}}" \
                 "Publisher" "${{COMPANYNAME}}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${{APPNAME}}" \
                 "HelpLink" "${{WEBSITE}}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${{APPNAME}}" \
                 "DisplayVersion" "{VERSION}"

  ${{GetSize}} "$INSTDIR" "/S=0K" $0 $1 $2
  IntFmt $0 "0x%08X" $0
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${{APPNAME}}" \
                     "EstimatedSize" "$0"

  ;Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall {EXENAME}"
  
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
    
    ;Create shortcuts
    CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
    CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Uninstall {NAME}.lnk" "$INSTDIR\Uninstall {EXENAME}"
    CreateShortCut "$SMPROGRAMS\$StartMenuFolder\${{APPNAME}}.lnk" "$INSTDIR\{EXENAME}" "" "$INSTDIR\icon.ico" 0

  !insertmacro MUI_STARTMENU_WRITE_END

SectionEnd

;--------------------------------
;Descriptions

  
  ;Language strings
  LangString DESC_SecDummy ${{LANG_ENGLISH}} "{NAME} - Required" ;This is the description listed on checkbox part of the installer

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${{SecDummy}} $(DESC_SecDummy)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
;Uninstaller Section

Section "Uninstall"

  ;ADD YOUR OWN FILES HERE...
  
  Delete "$INSTDIR\Uninstall {EXENAME}"

{DELETEFILES}

  

  RMDir "$INSTDIR"
  
  !insertmacro MUI_STARTMENU_GETFOLDER Application $StartMenuFolder
    
  Delete "$SMPROGRAMS\$StartMenuFolder\Uninstall {NAME}.lnk"
  Delete "$SMPROGRAMS\$StartMenuFolder\${{APPNAME}}.lnk"
  RMDir "$SMPROGRAMS\$StartMenuFolder"

  DeleteRegKey /ifempty HKCU "Software\${{COMPANYNAME}}\${{APPNAME}}"
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${{APPNAME}}"

SectionEnd