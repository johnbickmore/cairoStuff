# An implementation of a Double-Edge Connected List
# from de Berg's Computational Geometry Book
# Intended for use with cairo

class Vertex(object):
    """ A Simple vertex for two dimension """
    
    def __init__(self,x,y,iEdge=None):
        self.x = x
        self.y = y
        self.incidentEdge = iEdge

#--------------------
class HalfEdge(object):
    """ A Canonical Half-Edge. Has an origin point, and a twin half-edge for its end point """
    
    def __init__(self, origin, twin=None):
        self.origin = origin
        self.twin = twin
        self.face = None
        self.next = None
        self.prev = None

    def setNext(self,nextEdge):
        self.next = nextEdge

    def setPrev(self,prevEdge):
        self.prev = prevEdge

    def getVertices(self):
        return (self.origin,self.twin.origin)
        
#--------------------
class Face(object):
    """ A Face with a start point for its outer component list, and all of its inner components """
    
    def __init__(self):
        #Starting point for bounding edges, going anti-clockwise
        self.outerComponent = []
        #Clockwise inner loops
        self.innerComponents = []
        
#--------------------
class DCEL(object):
    """ The total DCEL data structure, stores vertices, edges, and faces """
    
    def __init__(self):
        self.vertices  = []
        self.faces     = []
        self.halfEdges = []

    def newVertex(self,x,y):
        """ Get a new vertex """
        newVertex = Vertex(x,y)
        self.vertices.append(newVertex)
        return newVertex
    
    def newEdge(self,originVertex,twinVertex,face=None,twinFace=None,prev=None,prev2=None):
        """ Get a new half edge pair, after specifying its start and end.
            Can set the faces, and previous edges of the new edge pair. 
            Returns the outer edge """
        e1 = HalfEdge(originVertex,None)
        e2 = HalfEdge(twinVertex,e1)
        e1.twin = e2
        if face:
            e1.face = face
        if twinFace:
            e2.face = twinFace
        if prev:
            e1.prev = prev
            prev.next = e1
        if prev2:
            e2.prev = prev2
            prev2.next = e2
        self.halfEdges.extend([e1,e2])
        return e1
        
    def newFace(self):
        """ Creates a new face to link edges """
        newFace = Face()
        self.faces.append(newFace)
        return newFace

    def linkEdgesTogether(self,edges):
        for i,e in enumerate(edges):
            e.prev = edges[i-1]
            e.prev.next = e
    
    def setFaceForEdgeLoop(self,face,edge,isInnerComponentList=False):
        """ For a face and a list of edges, link them together
            If the edges are the outer components, just put the first edge in the face,
            Otherwise places all the edges in the face """
        start = edge
        current = edge.next
        if isInnerComponentList:
            face.innerComponents.append(start)
        else:
            face.outerComponent = start
        start.face = face
        while current is not start and current.next is not None:
            current.face = face
            current = current.next
            if isInnerComponentList:
                face.innerComponents.append(current)

            
        