from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GalleryName(models.Model):
	name = models.CharField(max_length=200,blank=False)
	user = models.ForeignKey(User, on_delete= models.PROTECT)
	def __str__(self):
		return '%s' %(self.name)

class GalleryImg(models.Model):
	GalleryName = models.ForeignKey(GalleryName,on_delete=models.PROTECT)
	images      = models.FileField(upload_to='Gallery_image',blank=False,null=False)

	def  __str__(self):
		return '%s' %(self.GalleryName)


# from django.db import models
# from django.contrib.auth.models import User
# from tinymce import models as tinymce_models
# from ckeditor.fields import RichTextField


# class Category(models.Model):
# 	user_id		 = models.ForeignKey(User, on_delete = models.PROTECT)
# 	category     = models.CharField(max_length=2000,blank = False, default=None)
# 	add_date	 = models.DateTimeField(auto_now_add=True)
# 	update_date	 = models.DateTimeField(auto_now=True)
# 	status       = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s' % (self.category) 


# class Subcategory(models.Model):
# 	user_id		 = models.ForeignKey(User, on_delete = models.PROTECT)
# 	category_id  = models.ForeignKey(Category, on_delete = models.PROTECT)
# 	subcategory  = models.CharField(max_length=2000,blank= False, default=None)
# 	add_date	 = models.DateTimeField(auto_now_add=True)
# 	update_date	 = models.DateTimeField(auto_now=True)
# 	status       = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s %s' % (self.category_id.category,self.subcategory) 



# class DesignerName(models.Model):
# 	user_id		= models.ForeignKey(User, on_delete = models.PROTECT)
# 	name 		= models.CharField(max_length=2000,blank = False, default=None,unique=True)
# 	add_date	= models.DateTimeField(auto_now_add=True)
# 	update_date	= models.DateTimeField(auto_now=True)
# 	add_nav     = models.BooleanField(default=False)
# 	status      = models.BooleanField(default=False)

# 	def __str__(self):
# 		return self.name


# class MasterStyle(models.Model):
# 	user_id		= models.ForeignKey(User, on_delete = models.PROTECT)
# 	style_no 	= models.CharField(max_length=2000,blank = False, unique=True)
# 	style_name 	= models.CharField(max_length=2000,blank = True,null=True, unique=True)
# 	add_date	= models.DateTimeField(auto_now_add=True)
# 	update_date	= models.DateTimeField(auto_now=True)
# 	status      = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s %s' % (self.style_no,self.style_name)


# class Product(models.Model):
# 	user_id		  = models.ForeignKey(User, on_delete = models.PROTECT)
# 	subcategory_id= models.ForeignKey(Subcategory,on_delete=models.PROTECT)
# 	designer      = models.ForeignKey(DesignerName,on_delete=models.PROTECT,blank=True,null=True)
# 	style         = models.ForeignKey(MasterStyle,on_delete=models.PROTECT,blank=True,null=True)
# 	description   = RichTextField(blank=False,default=None)
# 	specification = RichTextField(blank=True,default=None,null=True)
# 	delivery      =	RichTextField(blank=True,null=True)
# 	prices        = models.IntegerField(default='0')
# 	offer_prices  = models.IntegerField(blank=True,null=True)
# 	add_date	  = models.DateTimeField(auto_now_add=True)
# 	update_date	  = models.DateTimeField(auto_now=True)
# 	status        = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s %s' % (self.style,self.prices)


# class Productsize(models.Model):
# 	user_id	   = models.ForeignKey(User,on_delete = models.PROTECT)
# 	size       = models.CharField(max_length=500,blank=True,default=None,unique=True)
# 	add_date   = models.DateTimeField(auto_now_add=True)
# 	update_date= models.DateTimeField(auto_now=True)
# 	status     = models.BooleanField(default=False)

# 	def __str__(self):
# 		return self.size


# class Productcolor(models.Model):
# 	user_id	   = models.ForeignKey(User,on_delete = models.PROTECT)
# 	color      = models.CharField(max_length=500,blank=True,default=None,unique=True)
# 	add_date   = models.DateTimeField(auto_now_add=True)
# 	update_date= models.DateTimeField(auto_now=True)
# 	status     = models.BooleanField(default=False)
# 	def __str__(self):
# 		return self.color 


# class ProductQty(models.Model):
# 	style   = models.ForeignKey(MasterStyle,on_delete=models.PROTECT)
# 	color   = models.ForeignKey(Productcolor,on_delete=models.PROTECT,blank=True,null=True)
# 	size    = models.ForeignKey(Productsize,on_delete=models.PROTECT,blank=True,null=True)
# 	qty     = models.CharField(max_length=500,blank=True,default=None)
# 	status  = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s %s' % (self.id,self.style) 


# class ProductImages(models.Model):
# 	product= models.ForeignKey(Product,on_delete=models.PROTECT)
# 	images = models.FileField(upload_to='product_image',blank=True,null=True)
# 	status = models.BooleanField(default=False)

# 	def __str__(self):
# 		return str(self.product)

		

# class Homebelow(models.Model):
# 	user_id	   = models.ForeignKey(User,on_delete = models.PROTECT)
# 	title      = models.CharField(max_length=200,blank=False,null=False,unique=True)
# 	description= RichTextField(blank=False,default=None)
# 	add_date   = models.DateTimeField(auto_now_add=True)
# 	update_date= models.DateTimeField(auto_now=True)
# 	status     = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s' % (self.title) 


# class HomeCategory(models.Model):
# 	user_id	   = models.ForeignKey(User,on_delete = models.PROTECT)
# 	Homebelow  = models.ForeignKey(Homebelow,on_delete=models.PROTECT)
# 	category   = models.ForeignKey(Category,on_delete = models.PROTECT,blank=True,null=True)
# 	homecateg  = models.FileField(upload_to='home_image_category',blank=False,null=True)
# 	add_date   = models.DateTimeField(auto_now_add=True)
# 	update_date= models.DateTimeField(auto_now=True)
# 	status     = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s' % (self.Homebelow) 

# class HomeSubcat(models.Model):
# 	user_id	   = models.ForeignKey(User,on_delete = models.PROTECT)
# 	Homebelow  = models.ForeignKey(Homebelow,on_delete=models.PROTECT)
# 	subcategory= models.ForeignKey(Subcategory,on_delete = models.PROTECT,blank=True,null=True)
# 	homesubcat = models.FileField(upload_to='home_image_subcat',blank=False,null=True)
# 	add_date   = models.DateTimeField(auto_now_add=True)
# 	update_date= models.DateTimeField(auto_now=True)
# 	status     = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s' % (self.Homebelow) 


# class Carousel(models.Model):
# 	user_id		  = models.ForeignKey(User, on_delete = models.PROTECT)
# 	subcategory_id= models.ForeignKey(Subcategory,on_delete=models.PROTECT,blank=True,null=True)
# 	carouselimages= models.ImageField(upload_to='carousel_image',blank=False,null=True)
# 	add_date	  = models.DateTimeField(auto_now_add=True)
# 	update_date	  = models.DateTimeField(auto_now=True)
# 	status        = models.BooleanField(default=False)

# 	def __str__(self):
# 		return str(self.subcategory_id)


# class BlogCategory(models.Model):
# 	user_id		 = models.ForeignKey(User, on_delete = models.PROTECT)
# 	blog_title   = models.CharField(max_length=2000,blank = False, default=None)
# 	add_date	 = models.DateTimeField(auto_now_add=True)
# 	update_date	 = models.DateTimeField(auto_now=True)
# 	status       = models.BooleanField(default=False)

# 	def __str__(self):
# 		return '%s' % self.blog_title


# class BlogPost(models.Model):
# 	blogcategory= models.ForeignKey(BlogCategory,on_delete=models.PROTECT)
# 	blogimages  = models.FileField(upload_to='blog_image',blank=False,null=False)
# 	title       = models.CharField(max_length=100, unique=True)
# 	body        = RichTextField(blank=False,default=None)
# 	add_date	= models.DateTimeField(auto_now_add=True)
# 	update_date = models.DateTimeField(auto_now=True)
# 	status      = models.BooleanField(default=False)
# 	def __str__(self):
# 		return '%s' % self.title


# class Termuser(models.Model):
# 	user_id		= models.ForeignKey(User, on_delete = models.PROTECT)
# 	Documentuser= RichTextField(blank=False,default=None)
# 	add_date	= models.DateTimeField(auto_now_add=True)
# 	update_date = models.DateTimeField(auto_now=True)
# 	status      = models.BooleanField(default=False)
 
# 	def __str__(self):
# 		return '%s' % (self.id)
 
# class About(models.Model):
# 	user_id		= models.ForeignKey(User, on_delete = models.PROTECT)
# 	Aboutus     = RichTextField(blank=False,default=None)
# 	add_date	= models.DateTimeField(auto_now_add=True)
# 	update_date = models.DateTimeField(auto_now=True)
# 	status      = models.BooleanField(default=False)
 
# 	def __str__(self):
# 		return '%s' % (self.id)
 


# class Instablog(models.Model):
# 	user_id		= models.ForeignKey(User, on_delete = models.PROTECT)
# 	Instablog   = models.ImageField(upload_to='insta_image',blank=False,null=True)
# 	url_insta   = models.URLField(max_length=200,blank=False,null=True)
# 	add_date	= models.DateTimeField(auto_now_add=True)
# 	update_date = models.DateTimeField(auto_now=True)
# 	status      = models.BooleanField(default=False)
 
# 	def __str__(self):
# 		return '%s' % (self.id)
 

# class Designer(models.Model):
# 	user_id		= models.ForeignKey(User, on_delete = models.PROTECT)
# 	subcategory = models.OneToOneField(DesignerName,on_delete=models.PROTECT,unique=True)
# 	designer_img= models.ImageField(upload_to='designer_img',blank=False)
# 	add_date	= models.DateTimeField(auto_now_add=True)
# 	update_date = models.DateTimeField(auto_now=True)
# 	status      = models.BooleanField(default=False)
 
# 	def __str__(self):
# 		return '%s' % (self.id)


# class Homeword(models.Model):
# 	user_id		= models.ForeignKey(User, on_delete = models.PROTECT)
# 	words       = models.CharField(max_length=2000,blank = False)
# 	add_date	= models.DateTimeField(auto_now_add=True)
# 	update_date = models.DateTimeField(auto_now=True)
# 	status      = models.BooleanField(default=False)
 
# 	def __str__(self):
# 		return '%s' % (self.id)


