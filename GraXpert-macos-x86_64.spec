# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['./src/gui.py'],
    pathex=[],
    binaries=[],
    datas=[('./img/*', './img/'), ('./forest-dark.tcl', './'), ('./forest-dark/*', './forest-dark/')],
    hiddenimports=['PIL._tkinter_finder', 'tkinter'],
    hookspath=['./releng'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, 
    cipher=block_cipher)
splash = Splash(
    'img/graXpert_Startbadge_Tethys.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(pyz,
    a.scripts,
    splash,
    [],
    exclude_binaries=True,
    name='GraXpert',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='x86_64',
    codesign_identity=None,
    entitlements_file=None , icon='./img/Icon.ico')

coll = COLLECT(
    exe,
    a.binaries,
    Tree('locales', prefix='locales/'),
    a.zipfiles,
    a.datas,
    splash.binaries,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='GraXpert')

app = BUNDLE(coll,
            name='GraXpert.app',
            icon='./img/Icon.ico',
            bundle_identifier=None,
            info_plist={
                'CFBundleShortVersionString': 'RELEASE (SNAPSHOT)',
                'NSHighResolutionCapable': 'True'
            }
            )