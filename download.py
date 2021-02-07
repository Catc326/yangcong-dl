from os import system,path
from time import sleep
from requests import get


def download(urls,names,download_dir):
    if not path.exists('N_m3u8DL-CLI_v2.9.5.exe'):
        print('未检测到下载器,开始下载')
        exe = get(
            'https://download.ravizhan.workers.dev/?durl=https://github.com/nilaoda/N_m3u8DL-CLI/releases/download/2.9.5/N_m3u8DL-CLI_v2.9.5.exe').content
        with open('N_m3u8DL-CLI_v2.9.5.exe', 'wb') as f:
            f.write(exe)
            f.close()
        print('下载器下载完成')
    for i in range(0, len(urls)):
        urls[i] = urls[i].replace('\n', '')
    dic = chuli(urls,names)
    download_dir = './Downloads/' + download_dir
    print('视频将保存到'+download_dir)
    for i in range(0, len(urls)):
        print('\r进度:%d/%d' % (i + 1, len(urls)), end='')
        name = dic[urls[i].split('_')[1].split('.')[0]]
        vbs = '''
        set ws=createobject("wscript.shell")
        ws.run "1.bat",0
        wscript.quit
        '''
        # 使用vbs调用bat,实现bat后台运行
        order = 'N_m3u8DL-CLI_v2.9.5.exe '+urls[i]+' --saveName "'+str(i)+name+'" --enableDelAfterDone --workDir "'+download_dir+'"\nexit'
        with open('1.bat', 'w', encoding='utf-8') as f:
            f.write(order)
            f.close()
        with open('1.vbs', 'w', encoding='utf-8') as f:
            f.write(vbs)
            f.close()
        system('start 1.vbs')
        sleep(3.0)
    sleep(1.0)
    print('\n下载任务创建完成，请等待下载完成')
    input('按任意键退出')


def chuli(urls,names):
    dic = {}
    res = []
    for i in urls:
        i = i.split('_')[1].split('.')
        del i[-1]
        res.append(''.join(i))
    for i in range(0, len(res)):
        dic[res[i]] = names[i]
    return dic
