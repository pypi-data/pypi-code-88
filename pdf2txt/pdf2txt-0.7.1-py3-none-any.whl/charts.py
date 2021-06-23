from pdf2txt.utils import cluster_objects, get_type, get_partially_overlapping_objects, intersecting_edges, edge_intersect_text, \
    parse_value, is_ovarlaping_with_objects, cluster_objects2, get_partially_touching_objects, vertical_overlap_with_list, horizontal_overlap_with_list, vertical_overlap, horizontal_overlap
from statistics import mean
from pdf2txt.utils import BoundingBox, get_widthin_BoundingBox, get_BoundingBox_from_objects, contains_objects
import pandas as pd
from itertools import compress
from collections import Counter
from pdf2txt.doc_analyzer.img import show_rects_and_wait
from math import isclose, ceil


class Chart(BoundingBox):

    def __init__(self, left, top, right, bottom, graph_type, page, **kwargs):
        super().__init__(left, top, right, bottom, **kwargs)
        self.page=page
        self.graph_type=graph_type
        self.MAX_NB_DATAPOINTS=10

    def extract_chart_data(self):

        words=get_widthin_BoundingBox(self.page.tokens, self)
        if self.graph_type=='h':
            return self.extract_chart_data_horizontal(words)
        elif self.graph_type=='v':
            return self.extract_chart_data_vertical(words)

    def extract_chart_data_horizontal(self,  words):
        # parse graph data
        #suposes all values are positive
        data = []
        labels = []
        if len(words)==0 or len(self.components)==0:
            return {'dataframe': None,
                    'text': []}

        extra_words=[w for w in words if w.bottom <self.components[0].top or w.top >self.components[-1].bottom]

        max_component_width=max([c.width for c in self.components])

        for component in self.components:
            bbox = BoundingBox(left=component.left, right=component.left+max_component_width+10, top=component.top, bottom=component.bottom)
            value = get_partially_overlapping_objects(bbox, words)
            if len(value) > 0:
                value_t = value[0].Text
                data.append(parse_value(value_t.strip('%')))
            bbox = BoundingBox(left=self.left, right=component.right, top=component.top, bottom=component.bottom)
            value = get_partially_overlapping_objects(bbox, words)
            if len(value) > 0:
                labels.append(value[0].Text)
            else:
                labels.append("")

        df = pd.DataFrame(list(zip(labels, data)),
                          columns=['label', 'value'])
        if df.empty:
            df = None
        return {'dataframe': df,
                'text': extra_words}

    def extract_chart_data_vertical(self,  words):
        # parse graph data
        data = []
        labels = []

        top_graph=1000
        bottom_graph=0
        for component in self.components:
            bbox = BoundingBox(left=component.left, right=component.right, top=component.top, bottom=component.bottom + 10)

            values = get_partially_overlapping_objects(bbox, words)
            for value in values:
                value_t = value.Text
                value_f = parse_value(value_t.strip('%'))
                top_graph=min(top_graph, value.top)
                bottom_graph=max(bottom_graph, value.bottom)
                if get_type(value_f)=="Numeric":
                    data.append(value_f)
                else:
                    labels.append(value_t)

            if len(values) < 2:
                bbox = BoundingBox(left=component.left, right=component.right, top=component.top - 10,
                                   bottom=component.bottom)
                value = get_partially_overlapping_objects(bbox, words)
                if len(value) > 0:
                    top_graph = min(top_graph, value[0].top)
                    bottom_graph = max(bottom_graph, value[0].bottom)

                    value_t = value[0].Text
                    value_f = parse_value(value_t.strip('%'))
                    if get_type(value_f) =="Numeric":
                        data.append(value_t)
                    else:
                        labels.append(value_t)

        df = pd.DataFrame(list(zip(labels, data)),
                          columns=['label', 'value'])
        extra_words=[w for w in words if w.bottom <top_graph or w.top >bottom_graph]

        if df.empty:
            df = None
        return {'dataframe': df,
                'text': extra_words}


def valid_bar_element(rect):
    horizental=True if rect.width>rect.height else False

    if rect.height < 1 or rect.width<1 or rect.top<=0 or rect.bottom <=0:
        return False

    if horizental:

        return rect.height<70 and  rect.width<350
    else:
        return rect.width<70 and rect.height<350

def extract_charts(page, rect_threshold=4):

#    _all_retangles=[ rect for rect in page.rects if rect.fill and rect.non_stroking_color!=(1, 1, 1) and rect.non_stroking_color!=1]+[c for c in page.curves if len(c.pts)<=4]
    rectangles_=[ rect for rect in page.rects if rect.fill and valid_bar_element(rect) and rect.non_stroking_color!=(1, 1, 1) and rect.non_stroking_color!=1]+[c for c in page.curves if valid_bar_element(c) and len(c.pts)<=4]


    #sometimes there are duplicates in regtangle list due to pdf objects defined twice
    rectangles=[]
    for r in rectangles_:
        if not contains_objects(r, rectangles):
            rectangles.append(r)
#    rect_for_graphs = sorted(
#        [rect for rect in rectangles if
#         rect.fill and (200 > rect.width > 0.5 and 200 > rect.height > 0.5)], key=lambda l: l.top)
    rect_for_graphs=rectangles


#    show_rects_and_wait(page.lines, image=page.image.copy())
    edges = rects_to_edges(rect_for_graphs,rectangles_, page.tokens, rect_threshold=rect_threshold, page=page)

    graphs=[]
    for e in edges['v']: #horizontal graphs
        graphs.append(extract_chart_area(e, page, rect_for_graphs,graph_type='h'))

    for e in  edges['h']:
        graphs.append(extract_chart_area(e, page, rect_for_graphs, graph_type='v'))

    return graphs


def separate_edges_v(edge, min_separation=4, min_gap=4, min_separation_size=60):

    edge['components'] = sorted(edge['components'], key=lambda e: e.top)
    # if len(edge['components'])<3:
    #     return [edge]


    separations = []
    for i in range(0, len(edge['components']) - 1):
        separations.append(ceil(edge['components'][i + 1].top - edge['components'][i].bottom))

    separations=[s for s in separations if int(s)>=0]
    if len(separations)<1:
        return []
    most_frequent_separations = Counter([s for s in separations if s>=0]).most_common(2)
    if len(most_frequent_separations)==2:
        total_values=most_frequent_separations[0][1]+most_frequent_separations[1][1]
        score=abs((most_frequent_separations[0][1]/total_values)-(most_frequent_separations[1][1]/total_values))
    else:
        score=1

    most_frequent_separation=most_frequent_separations[0][0]
    if score<0.2 or most_frequent_separation==0:
        if len(most_frequent_separations)>1:
            most_frequent_separation=max([most_frequent_separations[0][0], most_frequent_separations[1][0]])

    if most_frequent_separation>min_separation_size:
        return []

    if len(separations) > min_separation:
        new_edges=[]
        idx_list = [idx + 1 for idx, val in
                    enumerate(separations) if val > min_gap * most_frequent_separation]
        start = 0

        for idx in idx_list:
            new_edges.append(build_axis_from_components(edge['components'][start:idx], direction='v'))
            start = idx
        new_edges.append(build_axis_from_components(edge['components'][start:], direction='v'))

        return new_edges
    else:
        return [edge]

def separate_edges_h(edge, words, min_separation=4, min_gap=5, min_separation_size=60):

    edge['components'] = sorted(edge['components'], key=lambda e: e.left)
 #   if len(edge['components'])<3:
 #       return [edge]


    separations = []

    for i in range(0, len(edge['components']) - 1):
        separations.append(ceil(edge['components'][i + 1].left - edge['components'][i].right))

    separations=[s for s in separations if int(s)>=0]
    if len(separations)<1:
        return []
    most_frequent_separations = Counter([s for s in separations if s>=0]).most_common(2)
    if len(most_frequent_separations)==2:
        total_values=most_frequent_separations[0][1]+most_frequent_separations[1][1]
        score=abs((most_frequent_separations[0][1]/total_values)-(most_frequent_separations[1][1]/total_values))
    else:
        score=1

    most_frequent_separation=most_frequent_separations[0][0]
    if score<0.2 or most_frequent_separation==0:
        if len(most_frequent_separations)>1:
            most_frequent_separation=max([most_frequent_separations[0][0], most_frequent_separations[1][0]])
    if most_frequent_separation>min_separation_size:
        return []

    if len(separations) > min_separation:
        new_edges=[]
        idx_list = [idx + 1 for idx, val in
                    enumerate(separations) if val > min_gap * most_frequent_separation]
        start = 0

        if len(idx_list)>0:
            for idx in idx_list:
                new_edges.append(build_axis_from_components(edge['components'][start:idx], direction='v'))
                start = idx
        elif edge_intersect_text(words, edge['axis']):
            intersection_text=edge_intersect_text(words, edge['axis'])
            for k in intersection_text:
                left_components = [c for c in edge['components'] if c.left < k.left]
                remaining_components = edge['components'] = [c for c in edge['components'] if c.left > k.right]
                new_edges.append(build_axis_from_components(left_components, direction='h'))
                new_edges.append(build_axis_from_components(remaining_components, direction='h'))
        else:
            new_edges.append(build_axis_from_components(edge['components'][start:], direction='v'))

        return new_edges
    else:
        return [edge]


def rects_to_edges(rectangles_for_charts, all_rectangles,  words, rect_threshold=4, page=None):
    """

    """

    rectangles = sorted(rectangles_for_charts, key=lambda l: l.top)



    # in case of vertcal charts
    by_left = cluster_objects2(rectangles, ["left", "height"], rel_tol=0, abs_tol=2)

    by_bottom = cluster_objects2(rectangles, ["bottom", "width"], rel_tol=0, abs_tol=2)
    by_top = cluster_objects2(rectangles, ["top", "width"], rel_tol=0, abs_tol=2)


    edges = {}

    if by_left is None:
        by_left = []
    if by_bottom is None:
        by_bottom = []
    if by_top is None:
        by_top = []

    by_left = list(filter(lambda x: len(x) >= rect_threshold, by_left))
    by_bottom = list(filter(lambda x: len(x) >= rect_threshold, by_bottom))
    by_top = list(filter(lambda x: len(x) >= rect_threshold, by_top))


    edges['v'] = []
    for rects in by_left:
        initial_edge = build_axis_from_edges(rects, all_rectangles, 'v')
#        show_rects_and_wait([initial_edge["axis"]], image.copy(), title="edges vertical", color=(255, 0, 0))

        if initial_edge is None:
            continue
        for edge in separate_edges_v(initial_edge):
            if len(edge['components'])<2:
                continue
            widths = set([int(r.right - r.left) for r in edge['components']])

            heights = set([int(r.bottom - r.top) for r in edge['components']])

            if len(heights) >= 2 and max(heights) / min(heights) > 1.25:
                continue
            if 1<len(widths) >= len(edge['components'])/2:
                edge["axis_line"]=get_line_for_edge(edge["axis"], page, orientaion='v')
                edges['v'].append(edge)

    edges['h'] = []
    for rects in by_top:
        initial_edge = build_axis_from_edges(rects, all_rectangles, 'h', direction='down')


        if initial_edge is None:
            continue
        # show_rects_and_wait([initial_edge["axis"]], image.copy(), title="edges vertical", color=(255, 0, 0))
        # show_rects_and_wait(initial_edge["components"], image.copy(), title="edges vertical", color=(0, 255, 0))

        for edge in separate_edges_h(initial_edge, words):
            if len(edge['components'])<2:
                continue

            widths = set([int(r.right - r.left) for r in edge['components']])

            heights = set([int(r.bottom - r.top) for r in edge['components']])

            if len(widths) >= 2 and max(widths) / min(widths) > 1.25:
                continue
            if 1<len(heights) >= len(edge['components'])/2:
                edge["axis_line"]=get_line_for_edge(edge["axis"], page, orientaion='h')
                edges['h'].append(edge)
    for rects in by_bottom:
        initial_edge = build_axis_from_edges(rects, all_rectangles, 'h')

        if initial_edge is None:
            continue
        # show_rects_and_wait([initial_edge["axis"]], image.copy(), title="edges vertical", color=(255, 0, 0))
        # show_rects_and_wait(initial_edge["components"], image.copy(), title="edges vertical", color=(0, 255, 0))

        for edge in separate_edges_h(initial_edge, words):
            if len(edge['components'])<2:
                continue

            widths = set([int(r.right - r.left) for r in edge['components']])

            heights = set([int(r.bottom - r.top) for r in edge['components']])

            if len(widths) >= 2 and max(widths) / min(widths) > 1.25:
                continue
            if 1<len(heights) >= len(edge['components'])/2:
                edge["axis_line"]=get_line_for_edge(edge["axis"], page, orientaion='h')
                edges['h'].append(edge)



    return edges

def get_line_for_edge(edge, page, orientaion='v'):
    lines=[]
    if orientaion=='v':
        lines=page.vertical_lines
        for line in lines:
            if isclose(line.left, edge.left, abs_tol=1):
                if vertical_overlap(line, edge):
                    return line

    elif orientaion=='h':
        lines=page.horizontal_lines
        for line in lines:
            if isclose(line.top, edge.top, abs_tol=1):
                if horizontal_overlap(line, edge):
                    return line

    else:
        raise ValueError("Worng orientation")

def rects_to_edge_bk(rectangles, words, rect_threshold=4):
    """
    Find (imaginary) vertical lines that connect the left, right, or
    center of at least `word_threshold` words.
    """
    # Find words that share the same left, right, or centerpoints
    by_left = cluster_objects2(rectangles, ["left",  "height"], rel_tol=0, abs_tol=2)
    by_bottom = cluster_objects(rectangles, "bottom", 2)
    by_top = cluster_objects(rectangles, "top", 2)
    if by_top:
        by_bottom+=by_top
    edges = {}
    # Find the points that align with the most words
    if by_left is None:
        by_left = []
    if by_bottom is None:
        by_bottom = []

    by_left = list(filter(lambda x: len(x) >= rect_threshold, by_left))
    by_bottom = list(filter(lambda x: len(x) >= rect_threshold, by_bottom))


    by_left2=[]
    for left in by_left:
#        print(get_BoundingBox_from_objects(left))
        heights=set(int(r.bottom-r.top) for r in left)
        widhs = set(int(r.right - r.left) for r in left)
        if len(heights)<2 and len(widhs)>=rect_threshold-1:
            by_left2.append(left)

    by_bottom2=[]
    for bottom in by_bottom:
        heights=set(int(r.bottom-r.top) for r in bottom)
        widths = set(int(r.right - r.left) for r in bottom)
        if len(widths)<2 and len(heights)>=rect_threshold-1:
            by_bottom2.append(bottom)

    edge = {}
    by_bottom=by_bottom2
    by_left=by_left2
    edges['h'] = []
    for rects in by_bottom:
        edge = build_axis_from_edges(rects, rectangles, 'h')
        heights = set([int(r.bottom - r.top) for r in edge['components']])
        average_width = mean([(r.right - r.left) for r in edge['components']])
        if len(heights) > 3 and average_width < 30:
            edges['h'].append(edge)

    edges['v'] = []
    for rects in by_left:
        edge = build_axis_from_edges(rects, rectangles, 'v')

        heights = set([int(r.right - r.left) for r in edge['components']])
        if len(heights) > 3:
            edges['v'].append(edge)

    intersection_text = intersecting_edges([e['axis'] for e in edges['v']], words, x_tolerance=-1, y_tolerance=1)

    # if the edge intersect text we typically crossed to an other chart or rectangle. We split and recompute
    for k, v in intersection_text.items():
        vertical = v['v'][0]
        top = k[1]
        for edge in edges['v']:
            if edge['axis'] == vertical:
                top_components = [c for c in edge['components'] if c.bottom < top]
                remaining_components = edge['components'] = [c for c in edge['components'] if c.top > top]
                if len(top_components) >= 3:
                    edge1 = build_axis_from_components(top_components, 'v')
                    if edge in edges['h']:
                        edges['h'].remove(edge)
                    edges['h'].append(edge1)
                if len(remaining_components) >= 3:  # create new edge
                    edge2 = build_axis_from_components(remaining_components, direction='v')
                    edges['v'].append(edge2)

    # Do the same on the horisental graphs

    intersection_text = intersecting_edges(words, [e['axis'] for e in edges['h']], x_tolerance=-1, y_tolerance=1)

    # if the edge intersect text we typically crossed to an other chart or rectangle. We split and recompute
    for k, v in intersection_text.items():
        vertical = v['h'][0]
        left = k[0]
        for edge in edges['h']:
            if edge['axis'] == vertical:
                top_components = [c for c in edge['components'] if c.left < left]
                remaining_components = edge['components'] = [c for c in edge['components'] if c.left > left]
                if len(top_components) >= 3:
                    edge1 = build_axis_from_components(top_components, direction='h')
                    edges['h'].remove(edge)
                    edges['h'].append(edge1)
                if len(remaining_components) >= 3:  # create new edge
                    edge2 = build_axis_from_components(remaining_components, 'h')
                    edges['h'].append(edge2)

    intersection_data = intersecting_edges([e['axis'] for e in edges['v']], [e['axis'] for e in edges['h']],
                                           x_tolerance=-1, y_tolerance=1)
    intersections = set(
        [v['v'][0] for k, v in intersection_data.items()] + [v['h'][0] for k, v in intersection_data.items()])

    edges['v'] = [e for e in edges['v'] if e['axis'] not in intersections and e["bbox"].bottom-e["bbox"].top >60]
    edges['h'] = [e for e in edges['h'] if e['axis'] not in intersections and e["bbox"].right-e["bbox"].left >60]

    return edges


def build_axis_from_edges(edge_rects, all_rectangles, orientation='h', direction='up', min_bar_width=3):
    edge = {}

    if orientation == 'h' and direction=='up':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in edge_rects)-2*edge_rects[0].width,
                                   right=max(rect.right for rect in edge_rects)+2*edge_rects[0].width,
                                   top=min(rect.bottom for rect in edge_rects),
                                   bottom=min(rect.bottom for rect in edge_rects))
        edge['orientation'] = 'h'
    elif orientation == 'h' and direction=='down':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in edge_rects)-2*edge_rects[0].height,
                                   right=max(rect.right for rect in edge_rects)+2*edge_rects[0].height,
                                   top=min(rect.top for rect in edge_rects),
                                   bottom=min(rect.top for rect in edge_rects))
        edge['orientation'] = 'h'
    elif orientation == 'v':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in edge_rects),
                                   right=min(rect.left for rect in edge_rects),
                                   top=min(rect.top for rect in edge_rects) - 2*edge_rects[0].height,
                                   bottom=max(rect.bottom for rect in edge_rects) + 2*edge_rects[0].height)

        edge['orientation'] = 'v'
    else:
        raise Exception("wrong direction. Should be either 'h' for horizontal  or 'v' for vertical")

    edge['components'] = get_partially_touching_objects(edge['axis'], all_rectangles)
    #if edge is vertical, chart are supposed to be horizontal, so remove all retangle with no height as they are only lines
    if edge['orientation'] == 'v':
        edge['components']=[c for c in edge['components'] if c.height>min_bar_width and  not vertical_overlap_with_list(c,edge['components'])]


    #apply the same logic to horizontal axis/Veertical bars
    if edge['orientation'] == 'h':
        edge['components']=[c for c in edge['components'] if c.width>min_bar_width and  not horizontal_overlap_with_list(c,edge['components'])]


    #sort by largest
    edge['components']= sorted(list(set(edge['components'])), key=lambda c: -(c.width*c.height))

    is_inside=[not e1.contains(e2) for (e1, e2) in zip(edge['components'][:-1], edge['components'][1:])]
    is_inside.append(True)

    edge['components']=list(compress(edge['components'], is_inside))

    if len(edge['components'])==0:
        return None

    edge['bbox'] = BoundingBox(left=min(rect.left for rect in edge['components']),
                               right=max(rect.right for rect in edge['components']),
                               top=min(rect.top for rect in edge['components']),
                               bottom=max(rect.bottom for rect in edge['components']))

    if edge['orientation'] == 'v':
        edge['axis'].bottom = max(rect.bottom for rect in edge['components'])
        edge['axis'].top = min(rect.top for rect in edge['components'])

    elif edge['orientation'] == 'h':
        edge['axis'].left = min(rect.left for rect in edge['components'])
        edge['axis'].right= max(rect.right for rect in edge['components'])



    return edge


def build_axis_from_components(componenets, direction='h'):
    edge = {}

    if direction == 'h':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in componenets),
                                   right=max(rect.right for rect in componenets),
                                   top=min(rect.bottom for rect in componenets),
                                   bottom=min(rect.bottom for rect in componenets))
        edge['orientation'] = 'h'
    elif direction == 'v':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in componenets),
                                   right=min(rect.left for rect in componenets),
                                   top=min(rect.top for rect in componenets),
                                   bottom=max(rect.bottom for rect in componenets))
        edge['orientation'] = 'v'

    edge['components'] = componenets
    edge['bbox'] = BoundingBox(left=min(rect.left for rect in edge['components']),
                               right=max(rect.right for rect in edge['components']),
                               top=min(rect.top for rect in edge['components']),
                               bottom=max(rect.bottom for rect in edge['components']))

    return edge

def extract_chart_area(edge, page, rectangles, graph_type):

#    show_rects_and_wait([edge['bbox']], image=page.image.copy())
    if edge["axis_line"]:
        bbox = [edge['bbox'],edge["axis_line"]]
    else:
        bbox= [edge['bbox']]
    edge['bbox'] = BoundingBox(left=min([b.left for b in bbox]), top=min(([b.top for b in bbox])), right=max([b.right for b in bbox]), bottom=max(([b.bottom for b in bbox])))

    bbox=edge['bbox']
    bbox_left = BoundingBox(left=bbox.left, top=bbox.top, right=bbox.left, bottom=bbox.bottom)
    bbox_right = BoundingBox(left=bbox.right, top=bbox.top, right=bbox.right, bottom=bbox.bottom)
    bbox_top = BoundingBox(left=bbox.left, top=bbox.top, right=bbox.right, bottom=bbox.top)
    bbox_bottom = BoundingBox(left=bbox.left, top=bbox.bottom, right=bbox.right, bottom=bbox.bottom)


#    show_rects_and_wait([edge['bbox']], image=page.image.copy())

    step_size=10

    edge['bbox'].top -= step_size
    bbox_top.top -= step_size
    bbox_top.bottom -= step_size


    edge['bbox'].left -= step_size
    bbox_left.left -= step_size
    bbox_left.right -= step_size

    edge['bbox'].right += step_size
    bbox_right.right += step_size
    bbox_right.left += step_size

    edge['bbox'].bottom += step_size
    bbox_bottom.bottom += step_size
    bbox_bottom.top += step_size

    while is_ovarlaping_with_objects(bbox_top, page.tokens):
        edge['bbox'].top -= step_size
        bbox_top.top -= step_size
        bbox_top.bottom -= step_size
#        show_rects_and_wait([edge['bbox']], image=page.image.copy())

    while is_ovarlaping_with_objects(bbox_left, page.tokens):
        edge['bbox'].left -= step_size
        bbox_left.left -= step_size
        bbox_left.right -= step_size
 #       show_rects_and_wait([edge['bbox']], image=page.image.copy())


    while is_ovarlaping_with_objects(bbox_right, page.tokens):
        edge['bbox'].right += step_size
        bbox_right.right += step_size
        bbox_right.left += step_size
 #       show_rects_and_wait([edge['bbox']], image=page.image.copy())

    while is_ovarlaping_with_objects(bbox_bottom, page.tokens):
        edge['bbox'].bottom += step_size
        bbox_bottom.bottom += step_size
        bbox_bottom.top += step_size
#        show_rects_and_wait([edge['bbox']], image=page.image.copy())

    edge['axis'].top=edge['bbox'].top
    edge['axis'].bottom=edge['bbox'].bottom

#    edge['components']=get_partially_overlapping_objects(edge['bbox'], rectangles)
    return Chart(left=edge['bbox'].left, right=edge['bbox'].right, top=edge['bbox'].top, bottom=edge['bbox'].bottom, page=page, graph_type=graph_type, **edge)


def extract_chart_area_bk(edge, page, rectangles, graph_type):
    # parse graph data
    NB_POINTS = 20

    bbox = edge['bbox']
    bbox_left = BoundingBox(left=bbox.left, top=bbox.top, right=bbox.left, bottom=bbox.bottom)
    bbox_right = BoundingBox(left=bbox.right, top=bbox.top, right=bbox.right, bottom=bbox.bottom)
    bbox_top = BoundingBox(left=bbox.left, top=bbox.top, right=bbox.right, bottom=bbox.top)
    bbox_bottom = BoundingBox(left=bbox.left, top=bbox.bottom, right=bbox.right, bottom=bbox.bottom)


    i = 0
    while not is_ovarlaping_with_objects(bbox_top, page.tokens) and i < NB_POINTS/2:
        edge['bbox'].top -= 1
        bbox_top.top -= 1
        bbox_top.bottom -= 1
        i += 1

    if i == NB_POINTS:
        # we did not find any text redude the area by 10
        edge['bbox'].top += NB_POINTS
    if i < NB_POINTS:
        # once you touch text continue until you passed it

        while is_ovarlaping_with_objects(bbox_top, page.tokens):
            edge['bbox'].top -= 1
            bbox_top.top -= 1
            bbox_top.bottom -= 1

    # move left until we meet left axis text within max distance of 20 points
    i = 0
    while not is_ovarlaping_with_objects(bbox_left, page.tokens) and i < NB_POINTS:
        edge['bbox'].left -= 1
        bbox_left.left -= 1
        bbox_left.right -= 1
        i += 1

    if i == NB_POINTS:
        # we did not find any text redude the area by 10
        edge['bbox'].left += NB_POINTS
    if i < NB_POINTS:
        # once you touch text continue until you passed it

        while is_ovarlaping_with_objects(bbox_left, page.tokens):
            edge['bbox'].left -= 1
            bbox_left.left -= 1
            bbox_left.right -= 1

    i = 0
    while not is_ovarlaping_with_objects(bbox_right, page.tokens) and i < int(NB_POINTS / 2):
        edge['bbox'].right += 1
        bbox_right.right += 1
        bbox_right.left += 1

        i += 1

    if i < NB_POINTS:
        # once you touch text continue until you passed it

        while is_ovarlaping_with_objects(bbox_right, page.tokens):
            edge['bbox'].right += 1
            bbox_right.left += 1
            bbox_right.right += 1

    i = 0
    while not is_ovarlaping_with_objects(bbox_bottom, page.tokens) and i < NB_POINTS/2:
        edge['bbox'].bottom += 1
        bbox_bottom.bottom += 1
        bbox_bottom.top += 1
        i += 1
        show_rects_and_wait([edge['bbox']], image=page.image.copy())
    if i == NB_POINTS:
        # we did not find any text redude the area by 10
        edge['bbox'].bottom -= NB_POINTS/4
    if i == 0:
        edge['bbox'].bottom += NB_POINTS/4
        bbox_bottom.bottom += NB_POINTS/4
        bbox_bottom.top += NB_POINTS/4
    if i < NB_POINTS:
        # once you touch text continue until you passed it

        while is_ovarlaping_with_objects(bbox_bottom, page.tokens):
            edge['bbox'].bottom += 1
            bbox_bottom.bottom += 1
            bbox_bottom.top += 1
            show_rects_and_wait([edge['bbox']], image=page.image.copy())

    while is_ovarlaping_with_objects(
            BoundingBox(left=edge['bbox'].right, top=edge['bbox'].top, right=edge['bbox'].right,
                        bottom=edge['bbox'].bottom), page.tokens):
        edge['bbox'].right += 1
        bbox_bottom.right += 1
        bbox_bottom.left += 1

    edge['axis'].top=edge['bbox'].top
    edge['axis'].bottom=edge['bbox'].bottom

#    edge['components']=get_partially_overlapping_objects(edge['bbox'], rectangles)
    return Chart(left=edge['bbox'].left, right=edge['bbox'].right, top=edge['bbox'].top, bottom=edge['bbox'].bottom, page=page, graph_type=graph_type, **edge)
