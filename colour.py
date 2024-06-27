from vector import Vec3

def write_colour(pixel_colour: Vec3):
    r = pixel_colour.x
    g = pixel_colour.y
    b = pixel_colour.z

    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * B)

    return ("{ir} {ig} {ib}\n".format(ir=rbyte, ig=gbyte, ib=bbyte))


    vector = Vec3(1,1,1)
    print(write_colour(vector))