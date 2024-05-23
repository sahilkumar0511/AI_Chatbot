<?php
class Chatbot_API {
    public static function get_chatbot_response($query) {
        $response = wp_remote_post('http://your-backend-url/chat', array(
            'body' => json_encode(array('query' => $query)),
            'headers' => array('Content-Type' => 'application/json')
        ));

        if (is_wp_error($response)) {
            return array('error' => 'Unable to get response from chatbot');
        }

        $body = wp_remote_retrieve_body($response);
        return json_decode($body, true);
    }
}
?>