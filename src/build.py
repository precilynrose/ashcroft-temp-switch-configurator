#!/usr/bin/env python3
"""Builds the single self-contained HTML file: inlines the logo, photos (base64) and jsPDF."""
import base64, os
here = os.path.dirname(os.path.abspath(__file__))
def b64(path, mime):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(os.path.join(here, path), 'rb').read()).decode())
html = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
jspdf = open(os.path.join(here, 'jspdf.umd.min.js'), encoding='utf-8').read().replace('</script', '<\\/script')
html = (html.replace('__LOGO__', b64('assets/logo.png', 'image/png'))
            .replace('__T4__', b64('assets/t4.jpg', 'image/jpeg'))
            .replace('__T7__', b64('assets/t7.jpg', 'image/jpeg'))
            .replace('/*__JSPDF__*/', jspdf))
out = os.path.join(here, '..', 'ashcroft-temperature-switch-configurator.html')
open(out, 'w', encoding='utf-8').write(html)
print('built', os.path.abspath(out), round(len(html) / 1024), 'KB')
