# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['opening_UI.py','changeDate_UI.py','employee_UI.py','Employee.py','EmployeeList.py','otherEmployee_UI.py','readfile.py','view_UI.py'],
    pathex=[],
    binaries=[],
    datas=[('./2023工资单.xlsx','./'),('./w.png','./'),('./wj.png','./'),('./wjj.png','./')],
    hiddenimports=['PyiFrozenImporter','openpyxl.cell._writer'],
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
    name='工资计算器',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='工资计算器',
)
