# -*- mode: python -*-

block_cipher = None

a = Analysis(['bin/docker-compose'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='docker-compose',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

# Collect everything into a permanent folder
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               [
                   (
                       'compose/config/config_schema_v1.json',
                       'compose/config/config_schema_v1.json',
                       'DATA'
                   ),
                   (
                       'compose/config/compose_spec.json',
                       'compose/config/compose_spec.json',
                       'DATA'
                   ),
                   (
                       'compose/GITSHA',
                       'compose/GITSHA',
                       'DATA'
                   )
               ],
               strip=False,
               upx=False,
               upx_exclude=[],
               name='docker-compose')
