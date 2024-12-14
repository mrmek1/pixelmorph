from PyQt5.QtCore import QPropertyAnimation, QEasingCurve

def fade_in_animation(widget, duration=1000):
    opacity_effect = widget.graphicsEffect()
    fade_in = QPropertyAnimation(opacity_effect, b"opacity")
    fade_in.setDuration(duration)
    fade_in.setStartValue(0)
    fade_in.setEndValue(1)
    fade_in.start()

def button_click_animation(button):
    animation = QPropertyAnimation(button, b"geometry")
    animation.setDuration(200)
    animation.setStartValue(button.geometry())
    animation.setEndValue(button.geometry().adjusted(0, 0, 10, 10))
    animation.setEasingCurve(QEasingCurve.OutBounce)
    animation.start()

def slide_in_animation(widget, start_pos, end_pos, duration=500):
    animation = QPropertyAnimation(widget, b"pos")
    animation.setDuration(duration)
    animation.setStartValue(start_pos)
    animation.setEndValue(end_pos)
    animation.setEasingCurve(QEasingCurve.OutCubic)
    animation.start()

def fade_out_animation(widget, duration=1000):
    opacity_effect = widget.graphicsEffect()
    fade_out = QPropertyAnimation(opacity_effect, b"opacity")
    fade_out.setDuration(duration)
    fade_out.setStartValue(1)
    fade_out.setEndValue(0)
    fade_out.start()