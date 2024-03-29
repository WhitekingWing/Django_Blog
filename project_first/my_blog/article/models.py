from django.db import models
#导入内建的User模型
from django.contrib.auth.models import User
#timezone用于处理时间的相关业务
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from PIL import Image
from django.utils import timezone
# Create your models here.
class ArticleColumn(models.Model):
    """
    栏目的 Model
    """
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class ArticlePost(models.Model):
	#文章作者。参数on_delete用于指定数据删除的方式
	author = models.ForeignKey(User,on_delete = models.CASCADE)
	#文章标题。model.CharField为字符串字段，用于保存较短的字符串
	title = models.CharField(max_length=100)
	# 文章标签
	tags = TaggableManager(blank=True)
	avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
	#文章正文。保存大量文本用TextField
	body = models.TextField()
    # 新增点赞数统计
	likes = models.PositiveIntegerField(default=0)
	#文章创建时间。参数default=timezone.now指定在创建数据时将默认写入当前时间
	created = models.DateTimeField(default=timezone.now)
	#文章更新时间。参数auto_now=True指定每次数据更新时自动写入当前时间
	update = models.DateTimeField(auto_now=True)
	total_views = models.PositiveIntegerField(default=0)
	avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
	#内部类用于给model定义元数据
	column = models.ForeignKey(
        	ArticleColumn,
        	null=True,
       	 blank=True,
       	 on_delete=models.CASCADE,
    	  related_name='article'
    	 )
	class Meta:
		#ordering指定模型返回的数据的排列顺序
		#'-created'表明数据应该以倒序排序
		ordering = ('-created',)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
                                return reverse('article:article_detail', args=[self.id])
	# 保存时处理图片
	def save(self, *args, **kwargs):
    	# 调用原有的 save() 的功能
		article = super(ArticlePost, self).save(*args, **kwargs)

		# 固定宽度缩放图片大小
		if self.avatar and not kwargs.get('update_fields'):
			image = Image.open(self.avatar)
			(x, y) = image.size
			new_x = 400
			new_y = int(new_x * (y / x))
			resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
			resized_image.save(self.avatar.path)
		return article
	def was_created_recently(self):
		diff = timezone.now() - self.created
        
		# if diff.days <= 0 and diff.seconds < 60:
		if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
			return True
		else:
			return False