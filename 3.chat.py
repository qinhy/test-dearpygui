import dearpygui.dearpygui as dpg
import asyncio

# Callback to handle sending messages
def send_message_callback(sender, app_data, user_data):
    """
    Retrieves the user's message from the input widget,
    clears the input, and starts streaming the AI response.
    """
    user_message = dpg.get_value("input_text")
    if user_message.strip():
        # Display user's message in the main conversation area
        dpg.add_text(f"User: {user_message}", parent="conversation_area")
        
        # Clear the input field
        dpg.set_value("input_text", "")
        
        # Start streaming the AI response
        asyncio.run(stream_ai_reply())

async def stream_ai_reply():
    """
    Simulates streaming an AI response in chunks.
    """
    # Add a placeholder for the AI's message
    ai_message_tag = dpg.generate_uuid()
    dpg.add_text("ChatGPT: ", parent="conversation_area", tag=ai_message_tag, color=(150, 150, 150))
    print(ai_message_tag)
    
    # Simulated chunks of AI response
    simulated_response = [
        "Hello! ",
        "This is a streaming response ",
        "from the AI model. ",
        "Each part arrives ",
        "separately in real time."
    ]
    
    for chunk in simulated_response:
        await asyncio.sleep(0.5)  # Simulate delay between chunks
        current_text = dpg.get_value(ai_message_tag)
        # print(current_text)
        dpg.set_value(ai_message_tag, current_text + chunk)

# Create a theme with a dark style (optional)
def create_dark_theme():
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 30, 30), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Border, (128, 128, 128), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, (220, 220, 220), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 4, category=dpg.mvThemeCat_Core)
    return global_theme

dpg.create_context()

with dpg.window(label="ChatGPT Example GUI", width=900, height=600, tag="MainWindow"):
    with dpg.group(horizontal=True):
        with dpg.child_window(width=200, tag="sidebar", border=True):
            dpg.add_text("Sidebar/Project List:")
            dpg.add_button(label="Project 1")
            dpg.add_button(label="Project 2")
            dpg.add_button(label="Project 3")
        
        with dpg.child_window(width=-1, tag="main_content", border=False):
            with dpg.child_window(width=-1, height=-40, tag="conversation_area", border=True):
                dpg.add_text("ChatGPT: Welcome to the conversation!", color=(150, 150, 150))
            
            with dpg.group(horizontal=True):
                dpg.add_input_text(tag="input_text", hint="Type your message...", width=-70)
                dpg.add_button(label="Send", callback=send_message_callback)

# Apply dark theme
global_theme = create_dark_theme()
dpg.bind_theme(global_theme)

dpg.create_viewport(title='Dear PyGui Chat Example', width=920, height=640)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
