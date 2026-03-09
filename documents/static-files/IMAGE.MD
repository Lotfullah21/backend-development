## Image Upload Handling

The application uses Django's `ImageField` to handle image uploads for course thumbnails. The configuration for the `ImageField` is as follows:

```python
thumbnail = models.ImageField(upload_to="course_thumbnails/", blank=True, null=True)
```

### Upload Path Breakdown

Root Directory: The root directory for media files is defined in our settings.py with:

```bash
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

Subdirectory for Thumbnails: The `upload_to="course_thumbnails/"` argument specifies that uploaded images will be saved in a subfolder named course_thumbnails under MEDIA_ROOT.

### Final File Path

When an image is uploaded, it will be saved at:

```bash
/path/to/our/project/media/course_thumbnails/filename.extension
```

For example, if our BASE_DIR is `/home/myproject` and the file name is `example.jpg`, the image will be saved at:

```bash
/home/myproject/media/course_thumbnails/example.jpg
```

### Accessing Uploaded Files

To access the uploaded file in the application, Django will use the MEDIA_URL setting, which in our case is:

```bash
MEDIA_URL = '/media/'

```

So, if a user uploads an image named example.jpg, the image’s URL in our application would be:

```bash
http://127.0.0.1:8000/media/course_thumbnails/example.jpg

```

Django saves the uploaded file to MEDIA_ROOT plus any subdirectories specified in upload_to, making it accessible through the MEDIA_URL path in the application.
