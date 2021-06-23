def(width, height, title, content, window_bg, text_bg, text_fg, text_height, text_width):
	print("ha ha ha ha")

def execute_guimaker(self, exec_ctx):
        guiMaker.default(str(exec_ctx.symbol_table.get('width')), str(exec_ctx.symbol_table.get('height')), exec_ctx.symbol_table.get('title'), exec_ctx.symbol_table.get('content'), exec_ctx.symbol_table.get('window_bg'), exec_ctx.symbol_table.get('text_bg'), exec_ctx.symbol_table.get('text_fg'), exec_ctx.symbol_table.get('text_height'), exec_ctx.symbol_table.get('text_width'))
        return RTResult().success(Number.null)
# (width, height, title, content, window_bg, text_bg, text_fg, text_height, text_width)
    execute_guimaker.arg_names = ['width', 'height', 'title', 'content', ' window_bg', 'text_bg', 'text_fg', 'text_height', 'text_width']
# GUIMAKER("JJ") ['width', 'height',  exec_ctx.symbol_table.get('width'), exec_ctx.symbol_table.get('height')

