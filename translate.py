# coding:utf-8
# python 实现百度翻译
import os
import time
import requests
# import cchardet

# str1: 待翻译的句子
# from_lan: 源语言  zh:中文  en:英文
# to_lan:目标语言
def translate_lan(str1,from_lan,to_lan):
	data = {
		"to": to_lan, 
		"transtype": "translang", 
		"from": from_lan, 
		"simple_means_flag": "3", 
		"query": str1
	}

	headers = {
		"Origin": "http://fanyi.baidu.com", 
		"Content-Length": "65", 
		"Accept-Language": "zh-CN,zh;q=0.8", 
		"Accept-Encoding": "gzip, deflate", 
		"X-Requested-With": "XMLHttpRequest", 
		"Host": "fanyi.baidu.com", 
		"Accept": "*/*", 
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36", 
		"Connection": "keep-alive", 
		# "Cookie": "BAIDUID=79EEF3DEE4FD3A15BCC18FBD8CD8AFCD:FG=1; PSTM=1496411525; BIDUPSID=F15C3E5D85051380C263EA0F019EEF25; BDUSS=TM3MXZBekN6SzYtd1pTd3VKMXNLWVZGSkJveE42M3FGcjQxVlZBS2Itejg0Z0phTVFBQUFBJCQAAAAAAAAAAAEAAADDG0opsbHOs9LRsbFsb3ZlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPxV21n8VdtZb; __cfduid=d723f2ab9ff9b951b20425aed2927b9651508730843; MCITY=-%3A; BDSFRCVID=WNKsJeC629iAqY7AypzzuUx2J2GAyG5TH6aof_8QNuPZCMdF2l8LEG0PDf8g0Kubb20IogKKL2OTHmrP; H_BDCLCKID_SF=tJufoD-bJI_3eRjPMtQoqRt-KfrW54CXKKOLVMTHb4Okeq8CDl6Fjl_3jtQI0-nhbGTOoqA-BhOC_Uo2y5jHhUt_MGoPJMTO52O8of_M5KTpsIJMKJAWbT8U5f5Iab-eaKviah4-BMb1DtoMe6KMjToXeHttqbbfb-ofBnOXMtF_Hn7zepJFyntpbt-qJjc0066k_hjX-Pc0ff59DxCKQU_-QNonBT5KaKcdVUjkbxJAEp6gQ65SeMAkQN3T0PKO5bRiLRottDJzDn3oyUkKXp0nhq5TqtJHKbDD_K_KtxK; BDRCVFR[NcYAN-XwtoR]=mk3SLVN4HKm; PSINO=3; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1512031059; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1512031059; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D", 
		"Referer": "http://fanyi.baidu.com/translate", 
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
	}

	href='http://fanyi.baidu.com/v2transapi'

	res=requests.post(href,headers=headers,data=data)

	d=eval(res.content)

	results=d['trans_result']['data'][0]['dst']
	# print cchardet.detect(results)
	results=results.decode('unicode_escape','ignore')

	# unicode
	return results

source_path='corpus\EI-reg-English-Train\EI-reg-English-Train'
filenames=os.listdir(source_path)
print len(filenames)
print filenames

target_path='corpus\EI-reg-English-Train\EI-reg-English-Train_translated'
if not os.path.exists(target_path):
	os.mkdir(target_path)

for fname in filenames:
	lines=open(source_path+os.sep+fname).readlines()

	trans_lines=[]

	for i,line in enumerate(lines[:]):

		# str1='coffee the floor; And the soul grew furious as the stillness broken by little'
		pieces=line.strip().split('\t')
		sid=pieces[0]
		score=pieces[-1]
		str1=pieces[1]

		from_lan='en'
		to_lan='zh'
		results=translate_lan(str1,from_lan,to_lan)
		print fname,i
		time.sleep(0.2)

		# trans_lines.append(results.encode('utf-8','ignore'))

		f=open(target_path+os.sep+fname.split('.')[0]+'_trans.txt','a')
		# f.write('\n'.join(trans_lines))
		str2=sid+'\t'+results.encode('utf-8','ignore')+'\t'+score
		f.write(str2.replace('\n','-')+'\n')
		f.close()

