import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt
from time import time
# import plotly.graph_objs as go
 # import itertools


archive_url = "https://www.thrillophilia.com"
r = requests.get(archive_url)
soup = BeautifulSoup(r.content,'html.parser')

class scroller:
	# d = {}
	"""docstring for ClassName"""
	def __init__ (self, archive_url):
		# t=[""]
		self.archive_url=archive_url
		self.destination_k()
		self.countries_l()
		self.states_n()
		self.cities_m()
		# self.graph_data()


	def timer(func):
		def f(*args, **kwargs):
			before = time()
			rk = func(*args, **kwargs)
			after = time()
			print('elapsed', after-before)
			return rk
		return f
		 
	@timer	 
	def destination_k(self):
		dst = soup.find_all("a", {"data-group":"Popular Destinations"})
		for A in dst:
			#for i in A:
				#print(i)	
			  print(A.text)
	
	@timer		  
	def countries_l(self):
		ct = soup.find_all("div", {"class":"names-div inline-dropdown-anchors"})
		for each_countries in ct:
			  print(each_countries.text)

	@timer
	def states_n(self):
		st = soup.find_all("div", {"class":"col-md-12 activities-and-listings"})
		for each_states in st:
			for states in each_states.find_all('a', href=re.compile("^/states/")):
				  print(states.get('href'))

	@timer
	def cities_m(self):
		category=[]
		counter=[]
		Total_brought = [] 
		ci = soup.find_all("div", {"class":"col-md-8 inline-dropdown-anchors"})
		for each_cities in ci:
			for citiy in each_cities.find_all('a', href=re.compile("^/cities/")):
				city=archive_url+citiy.get('href')+"/things-to-do"
				request=requests.get(city)
				sou1=BeautifulSoup(request.content, 'lxml')
				print(city)

				catogaries_k= sou1.find_all("div", {"class":"filter-xor"})
				
				for jk in catogaries_k:
					# print(jk)
					catogaries = jk.text.split('(')[0]
					category.append(catogaries)
					print(catogaries)
					count = jk.text.split('(')[1].split(')')[0]
					# print(count)
					# counter.append(count)
					rl = requests.get(archive_url+jk.find("a").get("href"))
					so = BeautifulSoup(rl.content, "lxml")
					count1 = so.find_all("span", {"class":"sold"})

					total_p = []
					for brought in count1:
						pr = brought.text.split(':')[-1]
						total_p.append(int(pr))
					md = sum(total_p)
					print(md)
					Total_brought.append(md)
					counter.append(count)
				dataset = list(zip(category,counter, Total_brought))
				df=pd.DataFrame(data = dataset, columns = ['Activities', 'Total_Counter', 'Total_Brought'])
				print(df)

				# fd = category
				# xc = counter
				# fk = Total_brought
				# data = [plt.pie()]
				# x=['category', 'counter', 'Total_brought'],
				# y=[Activitie,Total_Counter , Total_Brought]
				# plt.iplot(data, filename='basic-bar')




				ax = df[['Total_Counter','Total_Brought']].plot(kind='bar', title ="data_analiaze", figsize=(15, 10), legend=True, fontsize=12)
				ax.set_xlabel("Total_Counter", fontsize=12)
				ax.set_ylabel("Total_brought", fontsize=12)
				plt.show()



				# data to plot

 
# create plot
				# fig, ax = plt.subplots()
				# index = category
				# opacity = 0.8
 
				# rects1 = plt.bar(index, xc, bar_width,
				#                  alpha=opacity,
				#                  color='b',
				#                  label='Frank')
 
				# rects2 = plt.bar(index + bar_width, fk, bar_width,
				#                  alpha=opacity,
				#                  color='g')
				 
				# plt.xlabel('counter')
				# plt.ylabel('Total_brought')
				# plt.title('data_staticks')
				# plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
				# plt.legend()
 
				# plt.tight_layout()
				# plt.show()


						

						# if "Featured" not in place:
						
						# if brought != None:
						# 	brought_text=brought.text
						# 	print("No. Tickets booked:",brought_text)
						# else:
						# 	print("No. Tickets booked:","Bought : 0")

						# print(place_brought)
						# place=place_brought.find_all("div", class_="name")
						# if "Featured" not in place:
						# 	print("Place Name:",place.text)

				# 	# brought=jk.find("span", class_="sold")
				# 	if brought != None:
				# 		brought_text=brought.text
				# 		print("No. Tickets booked:",brought_text)
				# 	else:
				# 		print("No. Tickets booked:","Bought : 0")

				# counter.append(count)
				# dataset = list(zip(category,counter))
				# df=pd.DataFrame(data = dataset, columns = ['Activities', 'Total_Count', 'Total_brought'])
				# print(df)

				# fd = category
				# fk = counter
				# plt.pie(fk,labels=fd)
				# # label = fd
				# plt.show()

        # dataset = list(zip(catagory_n)
        # df = pd.DataFrame(data = dataset, columns = ['Activities', 'Total_Count'])
        # df['Total_Bought'] = df['Total_Bought'].map({'Total_Bought': 1, 'Total_Bought': 0})
        # df['efficieny'] = 100*(df['Total_Bought']-df['Total_Count'])/df['Total_Bought']
        # print(df)
        # print("\n")






					# self.category_o()
		# self.soup = []
		# self.catogaries_k()
		#self.indian_subcontinents


					# print(,)
					# print(jk.text)

					# ra = archive_url+jk.find('a').get('href')

					# print(r
					# catagory_n=ra.split("/")[-3]
					# print(catagory_n,jk.text)
					# catagory_n=ra.split("/")[-1]
					# print(catagory_n.split('?')[0],jk.text)11
					# catagory_name = catagory_n
					# each_tags=get(ra)
					# bk = BeautifulSoup(catagory_name.content, "html.parser")
					# print(bk)
					# place_name_tags=soup.find_all("li", class_="grid-item case02")

					# for place_details in place_name_tags:
					# 	place=place_details.find("div", class_="name")
					# 	if "Featured" not in place:
					# 		print("Place Name:",place.text)


				# print(sou1)

	# def category_o(self):
	# 	catogaries_k= soup.find_all("div", {"class":"filter-xor"})
	# 	for jk in catogaries_k:
	# 		ra = archive_url+jk_.find('a').get('href')
	# 		print(jk)

#tags_each_place=archive_url+catogaries_n.find('a').get('href')

# tags = soup.find_all("div", {"class":"new-listing-type-page-filter-header"})
# for catogaries_k in jk:

#fk =archive_url+citiy.get('href')+"things-to-do"
		# soup = BeautifulSoup(each_place_url.content, "html.parser"





				# catagory_n=tags_each_place.split("/")[-1]
				# catagory_name =catagory_n
				# each_tags=get(tags_each_place)
				# so = BeautifulSoup(each_tags.content, "html.parser")
				# place_name_tags=soup.find_all("li", class_="grid-item case02")
				# for place_details in place_name_tags:
				# 	place=place_details.find("div", class_="name")
				# 	if "Featured" not in place:
				# 		print("Place Name:",place.text)







	# def catogaries_p(self):
		# #cat = soup.find_all("a", {"class":"indicator-target"})
		# catogaries=soup.find_all("div", class_="filter-xor")
		# for catogary_href in catogaries:
		 #	tags_each_place=archive_url+catogary_href.find('a').get('href')
		# 	print("catogary link:",tags_each_place)
		 #	catagory_n=tags_each_place.split("/")[-1]
		# 	catagory_name =catagory_n
		# 	each_tags=get(tags_each_place)
		# 	so = BeautifulSoup(each_tags.content, "html.parser")
		# 	place_name_tags=soup.find_all("li", class_="grid-item case02")


		# for mk in cat:
		# 	for active in activities.find_all("a", href=re.compile("^/Activity/")):
		# 		tags_each_place=archive_url+cat_href.find('a').get('href')
			#tags_each_place=url1+catogary_href.find('a').get('href')
				# print(active.get('href'))




	# def indian_subcontinents(self):
	# 	ind = soup.find_all("a", href="/" {"class":"header_activity_btn"})
	# 	for D in ind:

	# 		print(D.text)
obj = scroller(archive_url)
#obj.destination_k()