from django.db import models

# Create your models here.


def upload_location(instance,filename):
	return "{0}/{1}".format(instance.photo,filename)

def avatar_upload_location(instance,filename):
	return "{0}/{1}".format(instance.actress_name_ch,filename)

def banner_upload_location(instance,filename):
	return "{0}".format(filename)

class Series(models.Model):
	"""图片的分类"""
	#db_table = "Serie"
	text = models.CharField(max_length=40)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Photo(models.Model):
	"""图片集"""
	series = models.ForeignKey("Series",on_delete=models.PROTECT,null=False)	#欧美|日本|中国
	company = models.ForeignKey("Company",max_length = 60,null=True,blank=True,on_delete=models.PROTECT)	#公司
	name = models.CharField(max_length = 60)	#标题
	name_chinese = models.CharField(max_length=60)	#中文标题
	model_name = models.ManyToManyField("Actress")	#演员名
	date_added = models.DateTimeField(null=True,blank=True,auto_now_add=True)	#添加日期
	photo_tag = models.ManyToManyField("Tag",blank=True)	#标签
	views_count = models.PositiveIntegerField(default=0)	#点击量
	history_views_count = models.PositiveIntegerField(default=0)	#截至昨日点击量
	temperature = models.FloatField(default=0)	#相册热度
	"""照片购买"""
	vip_photo = models.BooleanField(default=False)	#是否付费
	buy_concent = models.CharField(max_length=60,null=True,blank=True)	#付费说明
	buy_price = models.IntegerField(null=True,blank=True)	#价格
	buy_link = models.CharField(max_length = 360,null=True,blank=True)	#购买链接
	"""Bundle购买"""
	vip_bundle = models.BooleanField(default=False)	#是否有Bundle
	bundle_concent = models.CharField(max_length=60,null=True,blank=True)	#Bundle说明
	bundle_price = models.IntegerField(null=True,blank=True)	#价格
	bundle_link = models.CharField(max_length = 360,null=True,blank=True)	#购买链接

	# cover_pic = Photo.PhotoFile.pic
	# cover_pic._meta.get_field('Photo').rel.to

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.name

	# def get_recommend_photo_cover_link(self):
	# 	current_name = 1
	# 	return current_name

	def get_cover_pic_link(self):
		current_name = self.id
		cover_pic_link = PhotoLink.objects.filter(photo=current_name).order_by('id')[0]
		return cover_pic_link.pic_link

	def get_actress_name(self):
		actress_name = self.model_name.all()

	def get_actress_id(self):
		actress = self.model_name.all()[0]
		actress = Actress.objects.get(actress_name_ch=actress)
		return actress.id

	# def get_right_recommend:
	# 	right_recommend = Photo.objects.all()[0:2]
	# 	return right_recommend

	def get_company_name(self):
		current_company = self.company

	def get_photo_id(self):
		return self.id

	def get_all_pic_link(self):
		current_name = self.id
		all_pic_links = PhotoLink.objects.filter(photo=current_name).order_by('id')
		detail_pic_links = []
		for all_pic_link in all_pic_links:
			detail_pic_links.append(all_pic_link.pic_link)
		return detail_pic_links

	def increase_views_count(self):
		self.views_count += 1
		self.save(update_fields=['views_count'])

	def get_absolute_url(self):
		return '/photo/%i' % self.id

class Actress(models.Model):
	actress_name_ch = models.CharField(max_length=60,null=True,blank=True)
	actress_name_jp = models.CharField(max_length=60,null=True,blank=True)
	actress_name_en = models.CharField(max_length=60,null=True,blank=True)
	avatar = models.ImageField(
							upload_to=avatar_upload_location,
							null=True,blank=True,
							)
	description = models.TextField(max_length=9999,null=True,blank=True)
	count_album = models.IntegerField(default=0)
	temperature = models.FloatField(default=0)
	#是否进入热搜标签池
	hot_search = models.BooleanField(default=False)

	def __str__(self):
		return self.actress_name_ch

	def get_all_photos(self):
		current_actress = self.actress_name_ch
		all_photos = Photo.objects.filter(model_name=current_actress)
		return all_photos

	def get_absolute_url(self):
		return '/actress_detail/%i' % self.id


class Tag(models.Model):
	"""相册标签"""
	tag_name = models.CharField(max_length = 20)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.tag_name

class Company(models.Model):
	"""公司标签"""
	company_name = models.CharField(max_length = 60)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.company_name


class PhotoFile(models.Model):
	pic = models.ImageField(
							upload_to=upload_location,
							null=True,blank=True,
							)
	photo = models.ForeignKey("Photo",on_delete=models.PROTECT,null=False)

class PhotoLink(models.Model):
	pic_link = models.CharField(max_length=1024)
	photo = models.ForeignKey("Photo",on_delete=models.PROTECT,null=False)

class SiteConfig(models.Model):
	config_name = models.CharField(default=None,max_length=100)
	config_value = models.CharField(default=None,max_length=100)

class SlideBanner(models.Model):
	banner_pic = models.ImageField(
							upload_to=banner_upload_location
							)
	banner_title = models.CharField(max_length=999)
	banner_link = models.CharField(max_length=999)