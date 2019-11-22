
# 文档相似性分析
from snownlp import SnowNLP
import jieba
import jieba.analyse
# 语料库准备
def text_corpus(text):
    s = SnowNLP(text)
    sents_list = []
    for sent_ in s.sentences:
        cut_list = jieba.cut(sent_, cut_all=False)
        sent_list = []
        for word in cut_list:
            sent_list.append(word)
        sents_list.append(sent_list)
    return sents_list  
# 待预测文档准备
def pre_process(sentence):
        cut_list = jieba.cut(sentence, cut_all=False)
        sent_list = []
        for word in cut_list:
            sent_list.append(word)
        return sent_list

def text_summary(text,number):
    s = SnowNLP(text)
    return s.summary(number)

def word_extract(text):
    word_list = []
    # for x, w in jieba.analyse.textrank(text, withWeight=True):
    for x, w in jieba.analyse.extract_tags(text, withWeight=True):
        word_list.append([x,w])
    return  word_list


# 语料库文档
corpus_text = u'''
使用snownlp进行情感分析。
文本情感分析。
语义分析之情感分析。
聊天机器人 , 中文翻译, 繁简 , 关键词提取 , 主题提取, 摘要提取 , 命名体识别, 分词 , 情感分析。
python的中文文本挖掘库snownlp进行购物评论文本情感分析实例。
'''

# 待预测文档
sent_predict = '中文翻译机器人聊天主题评论'

# 准备
sents_list = text_corpus(corpus_text)
print(sents_list)
sent_predict = pre_process(sent_predict)
print(sent_predict)
source_corpus = SnowNLP(sents_list)
# 相似性分析
print(source_corpus.sim(sent_predict))
# 文本摘要
print(text_summary(corpus_text,3))
#Tag 提取
text = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
print(word_extract(text))