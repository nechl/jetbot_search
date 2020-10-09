import time
from jetbot import Camera
from jetbot import ObjectDetector
from IPython.display import display
import ipywidgets.widgets as widgets
import outsourcing_nechl as myhelp
import cv2
from importlib import reload
import numpy as np
from jetbot import bgr8_to_jpeg
from jetbot import robot
def load_things():
    items={'0': ['background', '0', 'background'], '1': ['/m/01g317', '1', 'person'], '2': ['/m/0199g', '2', 'bicycle'], '3': ['/m/0k4j', '3', 'car'], '4': ['/m/04_sv', '4', 'motorcycle'], '5': ['/m/05czz6l', '5', 'airplane'], '6': ['/m/01bjv', '6', 'bus'], '7': ['/m/07jdr', '7', 'train'], '8': ['/m/07r04', '8', 'truck'], '9': ['/m/019jd', '9', 'boat'], '10': ['/m/015qff', '10', 'traffic light'], '11': ['/m/01pns0', '11', 'fire hydrant'], '12': ['12', '12', '12'], '13': ['/m/02pv19', '13', 'stop sign'], '14': ['/m/015qbp', '14', 'parking meter'], '15': ['/m/0cvnqh', '15', 'bench'], '16': ['/m/015p6', '16', 'bird'], '17': ['/m/01yrx', '17', 'cat'], '18': ['/m/0bt9lr', '18', 'dog'], '19': ['/m/03k3r', '19', 'horse'], '20': ['/m/07bgp', '20', 'sheep'], '21': ['/m/01xq0k1', '21', 'cow'], '22': ['/m/0bwd_0j', '22', 'elephant'], '23': ['/m/01dws', '23', 'bear'], '24': ['/m/0898b', '24', 'zebra'], '25': ['/m/03bk1', '25', 'giraffe'], '26': ['26', '26', '26'], '27': ['/m/01940j', '27', 'backpack'], '28': ['/m/0hnnb', '28', 'umbrella'], '29': ['29', '29', '29'], '30': ['30', '30', '30'], '31': ['/m/080hkjn', '31', 'handbag'], '32': ['/m/01rkbr', '32', 'tie'], '33': ['/m/01s55n', '33', 'suitcase'], '34': ['/m/02wmf', '34', 'frisbee'], '35': ['/m/071p9', '35', 'skis'], '36': ['/m/06__v', '36', 'snowboard'], '37': ['/m/018xm', '37', 'sports ball'], '38': ['/m/02zt3', '38', 'kite'], '39': ['/m/03g8mr', '39', 'baseball bat'], '40': ['/m/03grzl', '40', 'baseball glove'], '41': ['/m/06_fw', '41', 'skateboard'], '42': ['/m/019w40', '42', 'surfboard'], '43': ['/m/0dv9c', '43', 'tennis racket'], '44': ['/m/04dr76w', '44', 'bottle'], '45': ['45', '45', '45'], '46': ['/m/09tvcd', '46', 'wine glass'], '47': ['/m/08gqpm', '47', 'cup'], '48': ['/m/0dt3t', '48', 'fork'], '49': ['/m/04ctx', '49', 'knife'], '50': ['/m/0cmx8', '50', 'spoon'], '51': ['/m/04kkgm', '51', 'bowl'], '52': ['/m/09qck', '52', 'banana'], '53': ['/m/014j1m', '53', 'apple'], '54': ['/m/0l515', '54', 'sandwich'], '55': ['/m/0cyhj_', '55', 'orange'], '56': ['/m/0hkxq', '56', 'broccoli'], '57': ['/m/0fj52s', '57', 'carrot'], '58': ['/m/01b9xk', '58', 'hot dog'], '59': ['/m/0663v', '59', 'pizza'], '60': ['/m/0jy4k', '60', 'donut'], '61': ['/m/0fszt', '61', 'cake'], '62': ['/m/01mzpv', '62', 'chair'], '63': ['/m/02crq1', '63', 'couch'], '64': ['/m/03fp41', '64', 'potted plant'], '65': ['/m/03ssj5', '65', 'bed'], '66': ['66', '66', '66'], '67': ['/m/04bcr3', '67', 'dining table'], '68': ['68', '68', '68'], '69': ['69', '69', '69'], '70': ['/m/09g1w', '70', 'toilet'], '71': ['71', '71', '71'], '72': ['/m/07c52', '72', 'tv'], '73': ['/m/01c648', '73', 'laptop'], '74': ['/m/020lf', '74', 'mouse'], '75': ['/m/0qjjc', '75', 'remote'], '76': ['/m/01m2v', '76', 'keyboard'], '77': ['/m/050k8', '77', 'cell phone'], '78': ['/m/0fx9l', '78', 'microwave'], '79': ['/m/029bxz', '79', 'oven'], '80': ['/m/01k6s3', '80', 'toaster'], '81': ['/m/0130jx', '81', 'sink'], '82': ['/m/040b_t', '82', 'refrigerator'], '83': ['83', '83', '83'], '84': ['/m/0bt_c3', '84', 'book'], '85': ['/m/01x3z', '85', 'clock'], '86': ['/m/02s195', '86', 'vase'], '87': ['/m/01lsmm', '87', 'scissors'], '88': ['/m/0kmg4', '88', 'teddy bear'], '89': ['/m/03wvsk', '89', 'hair drier'], '90': ['/m/012xff', '90', 'toothbrush']}
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255,255,255)
    fontScale = 0.35
    thickness = 1
    return (items,font,color,fontScale,thickness)


def detectt(model,camera):
    detections = model(camera.value)
    return detections

def cam_stop(change):
    camera.unobserve_all()
    print("cam off")

def cam_start(change):
    camera.unobserve_all()
    camera.observe(execute, names="value")




def detection_center(detection):
    """Computes the center x, y coordinates of the object"""
    bbox = detection['bbox']
    center_x = (bbox[0] + bbox[2]) / 2.0 - 0.5
    center_y = (bbox[1] + bbox[3]) / 2.0 - 0.5
    return (center_x, center_y)
    
def norm(vec):
    """Computes the length of the 2D vector"""
    return np.sqrt(vec[0]**2 + vec[1]**2)
def closest_detection(detections):
    """Finds the detection closest to the image center"""
    closest_detection = None
    for det in detections:
        center = myhelp.detection_center(det)
        if closest_detection is None:
            closest_detection = det
        elif norm(myhelp.detection_center(det)) < norm(myhelp.detection_center(closest_detection)):
            closest_detection = det
    return closest_detection


    
def create_widgets(detections):
    button_layout = widgets.Layout(width="149px",height="100px")
    detections_widget = widgets.Textarea()
    button_stop_stream = widgets.Button(description="Stop the stream",button_style="danger", layout=button_layout)
    button_start_stream = widgets.Button(description = "start the stream", button_style="success", layout=button_layout)
    
    button_start_search = widgets.Button(description = "restart the search", button_style="success", layout=button_layout)
    button_stop_search = widgets.Button(description = "stop the search", button_style="danger", layout=button_layout)
    detections_widget.value = str(detections)
    label_widget=widgets.Dropdown(
    options=[],

    #rows=10,
    description='Detection of:',
    disabled=False,
    width="200px"
    )
    search_for_widget = widgets.Dropdown(
    options=[],

    #rows=10,
    description='Search of:',
    disabled=False,
    width="200px"
    )
    labeling=label_widget
    button_stream_box = widgets.HBox([button_stop_stream, button_start_stream])
    button_search_box = widgets.HBox([button_stop_search, button_start_search])
    
    return (button_stream_box, detections_widget, button_stop_stream, button_start_stream, labeling, search_for_widget, button_search_box, button_start_search, button_stop_search)

def fill_label(items, label_widget):
    for i in range(len(items)):
        label_widget.options=label_widget.options+(items[str(i)][2],)
    label_widget.value="background"

def check_selected_label(items,label_widget_value,detections):
    for item in range(len(items)):
        if items[str(item)][2]==label_widget_value:
            number_dett=int(items[str(item)][1])
    try:        
        matching_detections = [d for d in detections[0] if d['label'] == number_dett]
        det = myhelp.closest_detection(matching_detections)
        return det

    except NameError as NE:
        pass


def get_names(detections, items):
    all_labels=[]
    
    for item in detections[0]:
        
        all_labels.append(item['label'])
    all_labels = list(dict.fromkeys(all_labels))
    all_labels2names = []
    for i in items:
        if int(items[str(i)][1]) in all_labels:
            all_labels2names.append(items[str(i)][2])
    
    return(all_labels2names)