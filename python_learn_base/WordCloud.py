'''
wordcloud
pip3 install wordcloud
w=wordcloud.WordCloud()
w=wordcloud.WordCloud(width=400)
w=wordcloud.WordCloud(height=200)
w=wordcloud.WordCloud(min_font_size=4)
w=wordcloud.WordCloud(max_font_size)
w=wordcloud.WordCloud(font_size=1)
w=wordcloud.WordCloud(font_path=None)
w=wordcloud.WordCloud(max_words=200)
w=wordcloud.WordCloud(stop_words={""})
mask
	from scipy.misc import imread
	mk=imread("pic.png")
	w=wordcloud.WordCloud(mask=mk)
w=wordcloud.WordCloud(background_color="black")
w.generate(txt)
w.to_file(filename) .png .jpg
'''
import jieba
import wordcloud
txt="程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理"
w=wordcloud.WordCloud(width=1000,height=700,font_path="msyh.ttf")
w.generate(' '.join(jieba.lcut(txt)))
w.to_file("pywordcloud.png")