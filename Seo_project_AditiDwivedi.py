import re
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

url= input("ENTER THE URL :")
keyword=input("WHAT IS THE SEO KEWYWORD ?  ")
try:
   req=Request(url,headers={'User-Agent':'Mozilla/6.0'})
   html=urlopen(req)
except HTTPError as e:
   print (e)

data=BeautifulSoup(html,"html.parser")

def seo_title(keyword,data):
   if keyword.casefold() in data.title.text.casefold():
      status ='Found'
   else:
      status ='Not Found'
   return status

def seo_title_stop_words(data):
   words=0
   list_words=[]
   if data.title:
      with open('stopwords.txt','r') as f :
           for lines in f :
               if re.search(r'\b'+lines .rstrip('\n')+r'\b',data.title.text.casefold()):
                     words+=1
                     list_words.append(line.rstrip('\n'))
               if words>0:
                     stop_words='We found {} stop words in your  title .You should consider removing them '.format(words,list_words)
               else :
                     stop_words="We found no stop words in the title .Good Work ."

   else :
      stop_words="We could not find a title ."
   return stop_words

def seo_url(url):
   if url :
      if keyword in url:
         slug="Your keyword was found in your slug."
      else:
         slug="Your keyword was not found in your slug . It is suggested to add your keyword to your slug."

   else:
      slug="No url was returned."

   return slug

def seo_title_length(data):
   if data.title:
      if len(data.title.text)<60:
              length="Your length is under the maximum suggested length of 60 characters. Your title is  {} ". format(len(data.title.text))
      else :
              length="Your length is over the maximum suggest of 60 character.Your title is {}".format (len(data.title.text))
   else:
      length="No title was found . "
   return length


def seo_url_length(url):
   if url :
       if len(url)<100:
          url_length="Your URL is less than the 100 characters maximum suggested length . Good Work ."
       else :
          url_length="Your URL length is over 100 characters .Your URL currently is {} ".format(len(url))
   else :
       url_length="URL was not found."
   return url_length

def seo_h1(keyword,data):
   total_h1=0
   total_keyword_h1=0
   if data.h1:
       all_tags=data.find_all('h1')
       for tag in all_tags:
           total_h1+=1
           tag=str(tag.string)
           if keyword in tag.casefold():
                  total_keyword_h1+=1
                  h1_tag="Found keyword in h1 tag. You have a total {} h1 tags and your keyword was found in {} of them.".format(total_h1,total_keyword_h1)
           else:
                  h1_tag="Did not found a keyword in h1 tag . "
   else :
         h1_tag="No h1 tags found ."
   return h1_tag


def seo_h2(keyword,data):
   if data.h2:
       all_tags=data.find_all('h2')
       for tag in all_tags:
             tag=str(tag.string)
             if keyword in tag.casefold():
                h2_tag="Found your key word in atleast one h2 tag."
             else :
                h2_tag="We did not find your keyword in a single h2 tag .You should add {} to h2 tag .".format(keyword)
   else:
       h2_tag="NO h2 tags found .You should have atleast one containing your keyword ."
   return h2_tag

print (seo_title(keyword,data))
print (seo_title_stop_words(data))
print (seo_title_length(data))
print (seo_url(url))
print (seo_url_length(url))
print (seo_h1(keyword,data))
print (seo_h2(keyword,data))
