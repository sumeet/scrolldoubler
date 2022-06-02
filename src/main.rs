use inputbot::{MouseWheel, MouseButton, handle_input_events};

fn main() {
    MouseButton::OtherButton(4).bind(|| {
        println!("gotem");
        MouseButton::OtherButton(4).press();
        MouseButton::OtherButton(4).press();
    });
    MouseButton::OtherButton(5).bind(|| {
        println!("gotem");
        MouseButton::OtherButton(5).press();
        MouseButton::OtherButton(5).press();
    });
    handle_input_events()
}
