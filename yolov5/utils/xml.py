from xml.dom.minidom import Document  # write:

dict_ = {0:"fire", 1:"smoke"}


def write_xml(image, boxes, labels, image_name, anno_result_path=None):
    doc = Document()
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)

    folder = doc.createElement('folder')
    folder.appendChild(doc.createTextNode('fireSmoke'))
    annotation.appendChild(folder)

    filename = doc.createElement('filename')
    filename.appendChild(doc.createTextNode(image_name))
    annotation.appendChild(filename)

    source = doc.createElement('source')
    annotation.appendChild(source)

    database = doc.createElement('database')
    database.appendChild(doc.createTextNode('CameraDatabase'))
    source.appendChild(database)

    annotation1 = doc.createElement('annotation')
    annotation1.appendChild(doc.createTextNode('Camera Database'))
    source.appendChild(annotation1)

    sizes = list(image.shape)
    size = doc.createElement('size')
    annotation.appendChild(size)

    width = doc.createElement('width')
    width.appendChild(doc.createTextNode(str(sizes[1])))
    size.appendChild(width)

    height = doc.createElement('height')
    height.appendChild(doc.createTextNode(str(sizes[0])))
    size.appendChild(height)

    depth = doc.createElement('depth')
    depth.appendChild(doc.createTextNode(str(sizes[2])))
    size.appendChild(depth)

    segmented = doc.createElement('segmented')
    segmented.appendChild(doc.createTextNode('0'))
    annotation.appendChild(segmented)

    for box, label in zip(boxes, labels):
        coordinate = box

        object = doc.createElement('object')
        annotation.appendChild(object)

        name = doc.createElement('name')
        name.appendChild(doc.createTextNode(dict_[label]))
        object.appendChild(name)

        pose = doc.createElement('pose')
        pose.appendChild(doc.createTextNode('Unspecified'))
        object.appendChild(pose)

        truncated = doc.createElement('truncated')
        truncated.appendChild(doc.createTextNode('0'))
        object.appendChild(truncated)

        difficult = doc.createElement('difficult')
        difficult.appendChild(doc.createTextNode('0'))
        object.appendChild(difficult)

        bndbox = doc.createElement('bndbox')
        object.appendChild(bndbox)

        # 数字中包含序号，下标应从1开始
        xmin = doc.createElement('xmin')
        xmin.appendChild(doc.createTextNode(str(coordinate[0])))
        bndbox.appendChild(xmin)
        ymin = doc.createElement('ymin')
        ymin.appendChild(doc.createTextNode(str(coordinate[1])))
        bndbox.appendChild(ymin)
        xmax = doc.createElement('xmax')
        xmax.appendChild(doc.createTextNode(str(coordinate[2])))
        bndbox.appendChild(xmax)
        ymax = doc.createElement('ymax')
        ymax.appendChild(doc.createTextNode(str(coordinate[3])))
        bndbox.appendChild(ymax)

    f = open(image_name + ".xml", 'w')
    # exit(0)
    f.write(doc.toprettyxml(indent="\t"))
    f.close()
    # print(str(f) + " compelete")