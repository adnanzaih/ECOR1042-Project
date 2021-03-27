#Ayesha Dassanayake T010 101180472

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_height, get_color

def detect_edges(image: Image, threshold: int) -> Image:

    """
    Author: Ayesha Dassanayake
    
    Returns a new image with black and white pixels depending if the contrast is greater or less than the threshold
    >>> image = load_image(choose_file())
    >>> new_image = detect_edges(image,8)
    >>> show(new_image)
    """    
    
    edge_img = copy(image)

    black_pix = create_color(0,0,0)
    white_pix = create_color(255,255,255)
    
    height = get_height(edge_img) #height of the image
    
    for x,y,(r,g,b) in edge_img:
        top_pix = get_color(image,x,y) 
        rtop,gtop,btop = top_pix #colour components of the top pixel
        
        #executed if there is a bottom pixel
        if y < height - 1:
            btm_pix = get_color(image,x,y+1)
            rbtm,gbtm,bbtm = btm_pix #colour components of the bottom pixel
            
            top_avg = (rtop + gtop + btop)/3 
            btm_avg = (rbtm + gbtm + bbtm)/3
            
            contrast = abs(top_avg - btm_avg) #contrast that determines whether the pixel will be black or white
            
            if contrast > threshold:
                set_color(edge_img,x,y,black_pix) #pixel becomes black
            else:
                set_color(edge_img,x,y,white_pix) #pixel becomes white 
                
        else: 
            set_color(edge_img,x,y,white_pix) #pixel becomes white 
            
    return edge_img

if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = detect_edges(image,8)
    show(new_image)        
