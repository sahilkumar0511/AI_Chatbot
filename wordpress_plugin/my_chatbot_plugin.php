<?php
/*
Plugin Name: My Chatbot Plugin
Description: A plugin to integrate a chatbot with RAG and Chain of Thought.
Version: 1.0
Author: Your Name
*/

defined('ABSPATH') or die('No script kiddies please!');

define('CHATBOT_PLUGIN_PATH', plugin_dir_path(__FILE__));

require_once(CHATBOT_PLUGIN_PATH . 'includes/class-chatbot-api.php');

function chatbot_enqueue_scripts() {
    wp_enqueue_script('chatbot-interface', plugin_dir_url(__FILE__) . 'assets/chatbot-interface.js', array('jquery'), '1.0', true);
    wp_localize_script('chatbot-interface', 'chatbot_ajax', array('ajax_url' => admin_url('admin-ajax.php')));
}
add_action('wp_enqueue_scripts', 'chatbot_enqueue_scripts');

add_action('wp_ajax_nopriv_chatbot_query', 'chatbot_query_callback');
add_action('wp_ajax_chatbot_query', 'chatbot_query_callback');

function chatbot_query_callback() {
    $query = sanitize_text_field($_POST['query']);
    $response = Chatbot_API::get_chatbot_response($query);
    wp_send_json($response);
}
?>