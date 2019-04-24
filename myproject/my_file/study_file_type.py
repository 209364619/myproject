# coding=utf-8
import struct


# 参考博客：
#       https://www.cnblogs.com/chenjingyi/p/5741854.html
# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少半2字符，长则8字符
def typeList():
    return {
        "52617221": 'EXT_RAR',
        "504B0304": 'EXT_ZIP'}


# 字节码转16进制字符串
def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# 获取文件类型
def filetype(filepath):
    binfile = open(filepath, 'rb')  # 必需二制字读取
    tl = typeList()
    ftype = 'unknown'
    for hcode in tl.keys():
        numOfBytes = len(hcode) / 2  # 需要读多少字节
        binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
        hbytes = struct.unpack_from("B" * numOfBytes, binfile.read(numOfBytes))  # 一个 "B"表示一个字节
        f_hcode = bytes2hex(hbytes)
        if f_hcode == hcode:
            ftype = tl[hcode]
            break
    # 不要忘记关闭打开的文件，避免出现异常
    binfile.close()
    return ftype


if __name__ == '__main__':
    print filetype('C:\Users\y500\Desktop\ppt')

'''
附上常见文件二进制头标识

255044PDF 
526563 EML 
D0CF11 PPT 
4D5AEE COM 
E93B03 COM 
4D5A90 EXE 
424D3E BMP 
49492A TIF 
384250 PSD 
C5D0D3 EPS 
0A0501 PCS 
89504E PNG 
060500 RAW 
000002 TGA 
60EA27 ARJ 
526172 RAR 
504B03 ZIP 
495363 CAB 
1F9D8C Z 
524946 WAV 
435753 SWF 
3026B2 WMV 
3026B2 WMA 
2E524D RM 
00000F MOV 
000077 MOV 
000001 MPA 
FFFB50 MP3 
234558 m3u 
3C2144 HTM 
FFFE3C XSL 
3C3F78 XML 
3C3F78 MSC 
4C0000 LNK 
495453 CHM 
805343 scm 
D0CF11 XLS 
31BE00 WRI 
00FFFF MDF 
4D4544 MDS 
5B436C CCD 
00FFFF IMG 
FFFFFF SUB 
17A150 PCB 
2A5052 ECO 
526563 PPC 
000100 DDB 
42494C LDB 
2A7665 SCH 
2A2420 LIB 
434841 FNT 
7B5C72 RTF 
7B5072 GTD 
234445 PRG 
000007 PJT 
202020 BAS 
000002 TAG 
4D5A90 dll 
4D5A90 OCX 
4D5A50 DPL 
3F5F03 HLP 
4D5A90 OLB 
4D5A90 IMM 
4D5A90 IME 
3F5F03 LHP 
C22020 NLS 
5B5769 CPX 
4D5A16 DRV 
5B4144 PBK 
24536F PLL 
4E4553 NES 
87F53E GBC 
00FFFF SMD 
584245 XBE 
005001 XMV 
000100 TTF 
484802 PDG 
000100 TST
414331 dwg 
D0CF11 max

还有一些重要文件，没有固定头标识
TXT 没固定文件头定义 
TMP 没固定文件头定义 
INI 没固定文件头定义 
BIN 没固定文件头定义 
DBF 没固定文件头定义 
C 没没固定文件头定义 
CPP 没固定文件头定义 
H 没固定文件头定义 
BAT 没固定文件头定义 

还有一些不同的文件有相同的文件头，最典型的就是下面： 

4D5A90 EXE 
4D5A90 dll 
4D5A90 OCX 
4D5A90 OLB 
4D5A90 IMM 
4D5A90 IME
'''
