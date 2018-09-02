def _normalize_rect(rect):
    x1, y1, x2, y2 = rect
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    return (x1, y1, x2, y2)


class _QuadNode:
    def __init__(self, item, rect):
        self.item = item
        self.rect = rect


class _QuadTree:
    def __init__(self, x, y, width, height, depth=0, maxitems=10, maxdepth=20, _quadmap={}):
        self.nodes = []
        self.children = []
        self.center = [x, y]
        self.width, self.height = width, height
        self.depth = depth
        self.maxitems = maxitems
        self.maxdepth = maxdepth
        self._quadmap = _quadmap

    def __iter__(self):
        def loopallchildren(parent):
            for child in parent.children:
                if child.children:
                    for subchild in loopallchildren(parent=child):
                        yield subchild
                yield child

        for child in loopallchildren(self):
            yield child

    def _insert(self, item, bbox):
        rect = _normalize_rect(bbox)
        if len(self.children) == 0:
            node = _QuadNode(item, rect)
            self.nodes.append(node)
            if item in self._quadmap:
                self._quadmap[item].append((self.nodes, node))
            else:
                self._quadmap[item] = [(self.nodes, node)]
            if len(self.nodes) > self.maxitems and self.depth < self.maxdepth:
                self._split()
        else:
            self._insert_into_children(item, rect)

    def _intersect(self, bbox, results=None):
        rect = bbox
        if results is None:
            rect = _normalize_rect(rect)
            results = set()
        # search children
        if len(self.children) > 0:
            if rect[0] <= self.center[0]:
                if rect[1] <= self.center[1]:
                    self.children[0]._intersect(rect, results)
                if rect[3] > self.center[1]:
                    self.children[1]._intersect(rect, results)
            if rect[2] > self.center[0]:
                if rect[1] <= self.center[1]:
                    self.children[2]._intersect(rect, results)
                if rect[3] > self.center[1]:
                    self.children[3]._intersect(rect, results)
        # search node at this level
        for node in self.nodes:
            if (node.rect[2] > rect[0] and node.rect[0] <= rect[2] and
                    node.rect[3] > rect[1] and node.rect[1] <= rect[3]):
                results.add(node.item)
        return results

    def _insert_into_children(self, item, rect):
        # if rect spans center then insert here
        if ((rect[0] <= self.center[0] < rect[2]) and (rect[1] <= self.center[1] < rect[3])):
            node = _QuadNode(item, rect)
            self.nodes.append(node)
            if item in self._quadmap:
                self._quadmap[item].append((self.nodes, node))
            else:
                self._quadmap[item] = [(self.nodes, node)]
        else:
            # try to insert into children
            if rect[0] <= self.center[0]:
                if rect[1] <= self.center[1]:
                    self.children[0]._insert(item, rect)
                if rect[3] > self.center[1]:
                    self.children[1]._insert(item, rect)
            if rect[2] > self.center[0]:
                if rect[1] <= self.center[1]:
                    self.children[2]._insert(item, rect)
                if rect[3] > self.center[1]:
                    self.children[3]._insert(item, rect)

    def _remove(self, item):
        if item in self._quadmap:
            for quad_nodes_list, node in self._quadmap[item]:
                quad_nodes_list.remove(node)
            del self._quadmap[item]

    def _split(self):
        quartwidth = self.width / 4.0
        quartheight = self.height / 4.0
        halfwidth = self.width / 2.0
        halfheight = self.height / 2.0
        self.children = [_QuadTree(self.center[0] - quartwidth,
                                   self.center[1] - quartheight,
                                   width=halfwidth, height=halfheight,
                                   depth=self.depth + 1,
                                   maxitems=self.maxitems,
                                   maxdepth=self.maxdepth,
                                   _quadmap=self._quadmap),
                         _QuadTree(self.center[0] - quartwidth,
                                   self.center[1] + quartheight,
                                   width=halfwidth, height=halfheight,
                                   depth=self.depth + 1,
                                   maxitems=self.maxitems,
                                   maxdepth=self.maxdepth,
                                   _quadmap=self._quadmap),
                         _QuadTree(self.center[0] + quartwidth,
                                   self.center[1] - quartheight,
                                   width=halfwidth, height=halfheight,
                                   depth=self.depth + 1,
                                   maxitems=self.maxitems,
                                   maxdepth=self.maxdepth,
                                   _quadmap=self._quadmap),
                         _QuadTree(self.center[0] + quartwidth,
                                   self.center[1] + quartheight,
                                   width=halfwidth, height=halfheight,
                                   depth=self.depth + 1,
                                   maxitems=self.maxitems,
                                   maxdepth=self.maxdepth,
                                   _quadmap=self._quadmap)]
        nodes = self.nodes
        self.nodes = []
        for node in nodes:
            self._insert_into_children(node.item, node.rect)

def _interval_to_bbox(x_interval, y_interval):
        x1, x2 = x_interval
        y1, y2 = y_interval
        return x1, y1, x2, y2

class Index(_QuadTree):
    def __init__(self, x_interval, y_interval, maxitems=10, maxdepth=20):
        x1, x2, = x_interval
        y1, y2 = y_interval
        width, height = x2 - x1, y2 - y1
        midx, midy = x1 + width / 2.0, y1 + height / 2.0
        self.nodes = []
        self.children = []
        self.center = [midx, midy]
        self.width, self.height = width, height
        self.depth = 0
        self.maxitems = maxitems
        self.maxdepth = maxdepth
        self._quadmap = {}

    def insert(self, item, x_interval, y_interval):
        self._insert(item, _interval_to_bbox(x_interval, y_interval))

    def intersect(self, x_interval, y_interval):
        return self._intersect(_interval_to_bbox(x_interval, y_interval))

    def countmembers(self):
        size = 0
        for child in self.children:
            size += child.countmembers()
        size += len(self.nodes)
        return size

    def remove(self, item):
        self._remove(item)

    def update_intervals(self, item, x_interval, y_interval):
        self.remove(item)
        self.insert(item, x_interval, y_interval)




