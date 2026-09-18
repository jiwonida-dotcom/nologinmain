import sys
p=sys.argv[1]
s=open(p,encoding='utf-8').read()
old_start='.np-deal .head{background:#fff;color:#101828;box-shadow:inset 0 0 0 1px #ebe9f7,0 4px 14px rgba(91,75,255,.08)}\n'
old_end='.np-deal .head .tt{color:#101828}\n'
a=s.index(old_start); b=s.index(old_end)+len(old_end)
new='''/* 타임딜 헤드 — 진한 남보라 카드 (2026-09-18 2차) */
.np-deal .head{position:relative;overflow:hidden;background:linear-gradient(135deg,#332c66 0%,#241e4d 100%);color:#fff;box-shadow:0 8px 22px rgba(36,30,77,.28),0 1px 3px rgba(36,30,77,.2)}
.np-deal .head:before{content:"";position:absolute;right:-50px;top:-70px;width:200px;height:200px;border-radius:50%;background:radial-gradient(circle,rgba(139,124,248,.42) 0%,rgba(139,124,248,0) 68%);pointer-events:none}
.np-deal .head:after{content:"";position:absolute;left:-40px;bottom:-80px;width:160px;height:160px;border-radius:50%;background:radial-gradient(circle,rgba(99,85,255,.25) 0%,rgba(99,85,255,0) 68%);pointer-events:none}
.np-deal .head .c,.np-deal .head .arr{position:relative}
.np-deal .head .row{opacity:1}
.np-deal .head .tm{color:#fff;background:rgba(139,124,248,.32);box-shadow:inset 0 0 0 1px rgba(255,255,255,.16);padding:0 12px 0 8px;border-radius:99px;font-variant-numeric:tabular-nums;font-weight:700}
.np-deal .head .ppl{color:rgba(255,255,255,.72);justify-content:flex-end}
.np-deal .head .av span{border-color:#2a2458}
.np-deal .head .tt{color:#fff;font-weight:700}
.np-deal .head .arr svg circle{fill:rgba(255,255,255,.14)}
.np-deal .head:active{background:linear-gradient(135deg,#2c2659 0%,#1f1a42 100%)}
'''
s=s[:a]+new+s[b:]
open(p,'w',encoding='utf-8').write(s)
print('ok')
