import os, re, pathlib

root = pathlib.Path('.')
files = {}
for p in root.rglob('*.md'):
    files[p.stem] = p.relative_to(root).as_posix()

def conv(m):
    inner = m.group(1)
    if '#' in inner:
        name, anchor = inner.split('#', 1)
        target = None
        if name in files:
            target = files[name]
        elif name == '':
            return '[' + inner.replace('#', '') + '](#' + anchor + ')'
        else:
            for k, v in files.items():
                if k.lower() == name.lower():
                    target = v
                    break
        if target:
            return '[' + name + '#' + anchor + '](' + target + '#' + anchor + ')'
        return m.group(0)
    name = inner.strip()
    target = None
    if name in files:
        target = files[name]
    else:
        for k, v in files.items():
            if k.lower() == name.lower() or k.replace(' ', '_') == name.replace(' ', '_'):
                target = v
                break
    if target:
        return '[' + name + '](' + target + ')'
    return '[' + name + '](' + name + '.md)'

wikire = re.compile(r'\[\[([^\]]+)\]\]')
for p in root.rglob('*.md'):
    try:
        txt = p.read_text(encoding='utf-8')
    except Exception:
        try:
            txt = p.read_text(encoding='cp1251')
        except Exception:
            continue
    ntxt, n = wikire.subn(conv, txt)
    if n:
        p.write_text(ntxt, encoding='utf-8')
        print('updated', p)
