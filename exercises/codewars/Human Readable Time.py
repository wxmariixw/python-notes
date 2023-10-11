def make_readable(seconds):
    second = seconds % 60
    minutes = seconds // 60
    minute = minutes % 60
    hours = minutes // 60
    
    return f"{hours:02.0f}:{minute:02.0f}:{second:02.0f}"