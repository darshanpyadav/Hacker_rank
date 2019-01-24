import xml.etree.ElementTree as etree


def traverse(node):
  return len(node.attrib) + sum(traverse(child) for child in node)


xml = ''.join(input() for _ in range(int(input())))
tree = etree.ElementTree(etree.fromstring(xml))

print(traverse(tree.getroot()))


# ---------------------------------------------------------------------------------------------------------------------
maxdepth = -1


def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1

    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)