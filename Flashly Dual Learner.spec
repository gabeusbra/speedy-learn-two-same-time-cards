# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('/data/wordsToLearn.csv', '.'), ('/data/IT-FR-EN.csv', '.'), ('/audios/audio1.mp3', '.'), ('/audios/audio2.mp3', '.'), ('/audios/audio3.mp3', '.'), ('/audios/audio3.mp3', '.'), ('/images/card_front.png', '.'), ('/images/card_back.png', '.'), ('/images/sound42x42.png', '.'), ('/images/soundSmall.png', '.'), ('/images/wrong.png', '.'), ('/images/right.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Flashly Dual Learner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['images/F.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Flashly Dual Learner',
)
app = BUNDLE(
    coll,
    name='Flashly Dual Learner.app',
    icon='./images/F.ico',
    bundle_identifier=None,
)
