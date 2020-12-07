# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['E:\\User\\Desktop\\IA-metroAtenas\\src'],
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

a.datas +=[("data/distancias", "E:\\User\\Desktop\\IA-metroAtenas\\src\\data\\distancias", "DATA"),
             ("data/coordenadas", "E:\\User\\Desktop\\IA-metroAtenas\\src\\data\\coordenadas", "DATA"),
             ("image/1200px-Athens_Metro_Logo.svg.png", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\1200px-Athens_Metro_Logo.svg.png", "DATA"),
             ("image/circle_blue.png", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\circle_blue.png", "DATA"),
             ("image/circle_green.png", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\circle_green.png", "DATA"),
             ("image/circle_red.png", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\circle_red.png", "DATA"),
             ("image/circle_yellow.png", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\circle_yellow.png", "DATA"),
             ("image/flag-color.png", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\flag-color.png", "DATA"),
             ("image/mapa_metro_atenasCHULO.jpg", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\mapa_metro_atenasCHULO.jpg", "DATA"),
             ("image/mapa-color.png", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\mapa-color.png", "DATA"),
             ("image/route_icon_image.png", "E:\\User\\Desktop\\IA-metroAtenas\\src\\image\\route_icon_image.png", "DATA"),]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('W ignore', None, 'OPTION')],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon="image/metro.ico")
