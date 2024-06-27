from vector import Vec3, unit_vector
from ray import Ray

def ray_colour(r:Ray) -> Vec3:
    unit_direction = unit_vector(r.dir)
    a = 0.5 * (unit_direction.y + 1.0)
    return Vec3(1.0,1.0,1.0) * (1.0-a) + Vec3(0.5,0.7,1.0) * a


#Image
aspect_ratio = 16.0 / 9.0
image_width = 400

#calculate image height, ensure it is atleast 1
image_height = int(image_width / aspect_ratio)
image_height = 1 if image_height < 1 else image_height

#camera
focal_length = 1.0
viewport_height = 2.0
viewport_width = viewport_height * (float(image_width) / image_height)
camera_centre = Vec3(0,0,0)

#calculate the vectors across horizontal and vertical viewport edges
viewport_u = Vec3(viewport_width,0,0)
viewport_v = Vec3(0,-viewport_height,0)

#calculate horizontal and vertical delta from pixel to pixel
pixel_delta_u = viewport_u / image_width
pixel_delta_v = viewport_v / image_height

#calculate the location of upper left pixel
viewport_upper_left = camera_centre - Vec3(0,0,focal_length) - viewport_u/2 - viewport_v/2
pixel00_loc = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5 

#render
with open('ray.ppm', 'w') as f:
    f.write("P3\n{image_width} {image_height}\n255\n".format(image_width=image_width, image_height=image_height))

    for j in range(image_height):
        for i in range(image_width):
            pixel_centre = pixel00_loc + (pixel_delta_u * i) + (pixel_delta_v * j)
            ray_direction = pixel_centre - camera_centre
            ray = Ray(camera_centre, ray_direction)

            pixel_colour = ray_colour(ray)

            r = pixel_colour.x
            g = pixel_colour.y
            b = pixel_colour.z

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            f.write("{ir} {ig} {ib}\n".format(ir=ir, ig=ig, ib=ib))