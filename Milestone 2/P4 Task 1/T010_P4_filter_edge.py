#Ayesha Dassanayake T010 101180472

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_height

def detect_edges(image: Image, threshold: int) -> Image:

    """
    Author: Ayesha Dassanayake
    
    Returns a new image with black and white pixels depending if the contrast is greater or less than the threshold
    >>> image = load_image(choose_file())
    >>> new_image = detect_edges(image,15)
    >>> show(new_image)
    """    
    
    edge_img = copy(image)

    black_pix = create_color(0,0,0)
    white_pix = create_color(255,255,255)
    
    height = get_height(edge_img)
    
    for x,y,(r,g,b) in edge_img:
        og_color = create_color(r,g,b)
        top_pix = set_color(edge_img,x,y)
        rtop,gtop,btop = top_pix
        
        if y < height - 1:
            btm_pix = set_color(image,x,y+1,og_color)
            rbtm,gbtm,bbtm, btm_pix
            
            top_avg = (rtop + gtop + btop)/3
            btm_avg = (rbtm + gbtm + bbtm)/3
            
            contrast = abs(top_avg - btm_avg)
            
            if contrast > threshold:
                set_color(edge_img,x,y,black_pix)
                
        else: 
            set_color(edge_img,x,y,white_pix)
            
    return edge_img

if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = detect_edges(image,15)
    show(new_image)        