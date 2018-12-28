from django.db import models

# Create your models here.

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
	series = models.ForeignKey("Series",on_delete=models.PROTECT,null=False)
	company = models.ForeignKey("Company",max_length = 60,null=True,blank=True,on_delete=models.PROTECT)
	name = models.CharField(max_length = 60)
	name_chinese = models.CharField(max_length=60)
	actress_name = models.CharField(max_length=60,null=True,blank=True,)
	date_added = models.DateTimeField(null=True,blank=True,auto_now_add=True)
	photo_tag = models.ManyToManyField("Tag",blank=True)

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
		cover_pic_link = PhotoLink.objects.filter(photo=current_name)[0]
		return cover_pic_link.pic_link

	# def get_right_recommend:
	# 	right_recommend = Photo.objects.all()[0:2]
	# 	return right_recommend

	def get_photo_id(self):
		return self.id

	def get_all_pic_link(self):
		current_name = self.id
		all_pic_links = PhotoLink.objects.filter(photo=current_name)
		detail_pic_links = []
		for all_pic_link in all_pic_links:
			detail_pic_links.append(all_pic_link.pic_link)
		return detail_pic_links

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

def upload_location(instance,filename):
	return "{0}/{1}".format(instance.photo,filename)


class PhotoFile(models.Model):
	pic = models.ImageField(
							upload_to=upload_location,
							null=True,blank=True,
							)
	photo = models.ForeignKey("Photo",on_delete=models.PROTECT,null=False)

class PhotoLink(models.Model):
	pic_link = models.CharField(max_length=200)
	photo = models.ForeignKey("Photo",on_delete=models.PROTECT,null=False)