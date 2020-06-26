# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['.\\GUI\\operateWindow.py',
             '.\\handleCookie\\extract_chrome_cookie.py',
             '.\\handleCookie\\get_other_cookie.py',
             '.\\dataAnalysis\\getWebContent.py',
             '.\\GUI\\aboutDialog.py',
             '.\\GUI\\dangdangDialog.py',
             '.\\GUI\\detailDisplay.py',
             '.\\GUI\\helpDialog.py',
             '.\\GUI\\image.py',
             '.\\GUI\\loadingDialog.py',
             '.\\GUI\\mainWindow.py',
             '.\\GUI\\seachDialog.py'
             ],
             pathex=['G:\\Graduation Project\\Experiment\\MyCookieSoftware'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Cookie',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Cookie')
