from PyQt5.QtCore import Qt, QPoint, QSize, QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtSvg import QSvgRenderer


class QtSvgDocument:
    """Qt SVG document class"""

    def __init__(self):
        self._renderer = QSvgRenderer()
        self._size = self._renderer.defaultSize()

    def clear(self):
        """Clear the document"""
        self._renderer = QSvgRenderer()

    def setContent(self, text: str):
        """Set the content of the document"""
        success = self._renderer.load(text.encode())
        self._size = self._renderer.defaultSize()
        if not success:
            raise ValueError("Invalid SVG content")

    def setResizeFactor(self, factor: float):
        """Set the resize factor of the document"""
        self._size = self._size * factor

    def paint(self, p: QPainter, pos: QPoint):
        """Paint the document"""
        self._renderer.render(
            p, QRectF(pos.x(), pos.y(), self._size.width(), self._size.height())
        )

    def size(self) -> QSize:
        """Return the size of the document"""
        return self._size

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QMainWindow

    svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" width="1.924ex" height="1.902ex" viewBox="0 -683 850.3 840.8" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" style=""><defs><path id="MJX-17-TEX-C-49" d="M174 0H31Q-13 0 -21 2T-30 12Q-30 23 -17 36Q9 60 42 68L155 70Q187 102 214 179T257 333T302 491T366 610L369 614H305Q221 611 188 607T145 596T128 569Q119 543 94 529T47 512Q28 512 28 524Q28 527 32 539Q56 614 159 654Q218 678 312 682Q314 682 339 682T404 682T481 683H632Q642 678 642 671Q642 657 621 641T577 617Q570 615 507 614H444Q427 592 406 542Q382 478 355 366T310 209Q280 123 238 78L230 69H330Q442 70 442 74Q443 74 443 77T447 87T460 105Q490 134 527 137Q545 137 545 125Q545 120 542 112Q531 78 491 49T399 7Q379 2 360 2T174 0Z"></path><path id="MJX-17-TEX-I-1D461" d="M26 385Q19 392 19 395Q19 399 22 411T27 425Q29 430 36 430T87 431H140L159 511Q162 522 166 540T173 566T179 586T187 603T197 615T211 624T229 626Q247 625 254 615T261 596Q261 589 252 549T232 470L222 433Q222 431 272 431H323Q330 424 330 420Q330 398 317 385H210L174 240Q135 80 135 68Q135 26 162 26Q197 26 230 60T283 144Q285 150 288 151T303 153H307Q322 153 322 145Q322 142 319 133Q314 117 301 95T267 48T216 6T155 -11Q125 -11 98 4T59 56Q57 64 57 83V101L92 241Q127 382 128 383Q128 385 77 385H26Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><g data-mml-node="math"><g data-mml-node="msub"><g data-mml-node="TeXAtom" data-mjx-texclass="ORD"><g data-mml-node="mi"><use xlink:href="#MJX-17-TEX-C-49"></use></g></g><g data-mml-node="mi" transform="translate(545, -150) scale(0.707)"><use xlink:href="#MJX-17-TEX-I-1D461"></use></g></g></g></g></svg>
    """

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Qt SVG Example")
            self.resize(400, 400)

            self.document = QtSvgDocument()
            self.document.setContent(svg_content)

        def paintEvent(self, event):
            p = QPainter(self)
            self.document.paint(p, QPoint(0, 0))


    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()