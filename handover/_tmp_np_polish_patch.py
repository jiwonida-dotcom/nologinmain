import sys
p=sys.argv[1]
s=open(p,encoding='utf-8').read()
MARK='/* np-polish 2026-09-18 — 홈 스타일 고도화 (레이아웃 수치 유지 · 표면 스타일만) */'
assert MARK not in s, 'already applied'
css=MARK+'''
.np-bar i{background:#ececf1}
.np-menu button{transition:color .15s}
.np-menu button .ic{background:#f4f4f8;transition:background .15s,box-shadow .15s}
.np-menu button[aria-selected="true"] .ic{background:linear-gradient(150deg,#8a7bff,#6355ff);box-shadow:0 6px 14px rgba(99,85,255,.28)}
.np-menu button[aria-selected="true"]{color:#5b4bff;border-bottom-color:#5b4bff}
.np-banner{box-shadow:0 10px 28px rgba(99,93,255,.14),0 1px 3px rgba(99,93,255,.08);background:linear-gradient(154.15deg,#f1f0ff 0%,#e4e2ff 60%,#d8d4fe 100%)}
.np-slide .tag{background:rgba(255,255,255,.75);color:#5b4bff;box-shadow:0 1px 2px rgba(99,93,255,.12)}
.np-slide .img{background:rgba(255,255,255,.55);box-shadow:0 6px 18px rgba(99,93,255,.18)}
.np .np-more{background:linear-gradient(150deg,#8a7bff 0%,#5b4bff 100%);box-shadow:0 4px 12px rgba(91,75,255,.28)}
.np-login{background:linear-gradient(135deg,#f8f7ff 0%,#f1efff 55%,#ebe9fb 100%);box-shadow:inset 0 0 0 1px rgba(91,61,245,.08)}
.np-login .copy p{color:#1f1a45}
.np-login .btn{background:linear-gradient(150deg,#6d55ff,#5b3df5);box-shadow:0 6px 14px rgba(91,61,245,.24)}
.np-login .card{background:rgba(255,255,255,.88);border:1px solid rgba(91,61,245,.08);box-shadow:0 2px 8px rgba(91,61,245,.06)}
.np-login .card i{background:#ecebf8}
.np-deal .head{background:#fff;color:#101828;box-shadow:inset 0 0 0 1px #ebe9f7,0 4px 14px rgba(91,75,255,.08)}
.np-deal .head .row{opacity:1}
.np-deal .head .tm{color:#fff;background:linear-gradient(150deg,#6d55ff,#5b4bff);padding:0 12px 0 8px;border-radius:99px;font-variant-numeric:tabular-nums}
.np-deal .head .ppl{color:#6a7282;justify-content:flex-end}
.np-deal .head .av span{border-color:#fff}
.np-deal .head .tt{color:#101828}
.np-deal .body{background:#f7f7fb}
.np-sec .tit .h small{color:#6a7282;font-weight:500}
.np-sec .tit .h b{color:#101828;font-weight:700}
.np-sec .all{background:#f4f2ff;color:#5b4bff}
.np-chips button{border-color:#e5e5ec;color:#4a5565}
.np-chips button[aria-selected="true"]{background:linear-gradient(150deg,#7466ff,#5b4bff);border-color:#6355ff;box-shadow:0 4px 10px rgba(99,85,255,.25)}
.np-pdots button{background:#d9d7e8}.np-pdots button.on{background:#6355ff}
.np-plan,.np-phone{border-color:#ededf3;box-shadow:0 4px 14px rgba(16,24,40,.05)}
.np-plan .inc{background:#f4f4f8}
.np-plan .pr .n{color:#5b4bff}
.np-plan .bn{background:#f3f1ff;color:#5b4bff}
.np-phone .im{filter:drop-shadow(0 8px 14px rgba(0,0,0,.14))}
.np-phone .nm .g{border-color:#d9d9e3;color:#4a5565}
.np-phone .pr b{color:#5b4bff}
.np-bundle .b{border-color:#ececf1;box-shadow:0 4px 14px rgba(16,24,40,.05)}
.np-bundle p b{color:#5b4bff}
.np-cs .box{background:#fff;border-color:#ececf1;box-shadow:0 4px 14px rgba(16,24,40,.05)}
.np-cs .box button{border-bottom-color:#f1f1f5}
.np-cs .ico{filter:none;box-shadow:0 3px 8px rgba(16,24,40,.12)}
.np-totop button{border-color:#e5e5ec;filter:none;box-shadow:0 3px 8px rgba(16,24,40,.08)}
.np-deal .code .box{background:linear-gradient(150deg,#3d3670,#2b2450);box-shadow:0 12px 28px rgba(43,36,80,.22),0 2px 6px rgba(43,36,80,.12)}
.np-deal .pt{box-shadow:0 6px 16px rgba(91,61,245,.08),0 1px 3px rgba(91,61,245,.05)}
'''
anchor='.np-copy{'
i=s.index(anchor); j=s.index('\n',i)+1
s=s[:j]+css+s[j:]
open(p,'w',encoding='utf-8').write(s)
print('applied',len(css))
