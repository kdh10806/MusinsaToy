package com.toyproject2_5.musinsatoy.Item.product.service.chatbot;

import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

//RestTemplate은 동기식으로 통신  - 응답을 받을 때 까지 blocking , deprecated
//WebClient 는 Webflux 이해 필요 - webflux 까지 할 필요가 있나. 일단 하기.
public class ChatBotClientService {

    String url = "http://localhost:5000/";
    public Mono<?> chatBot(String message){

        System.out.println(message);

        WebClient webClient = WebClient.builder()
                .baseUrl(url)
                .defaultCookie("cookieKey","cookieValue")
                .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .build();

        Mono<?> resMono = webClient.post()
                .uri(url)
                .bodyValue(message)
//                .body(BodyInserters.fromValue(message))
                .retrieve()
                .bodyToMono(ChatDto.class);

        System.out.println(resMono);

//        resMono.subscribe(System.out::println);// 사용시 요청이 2번 보내짐. - 비동기 처리된 Mono에 한 번더 요청 발생.


        return resMono;
    }

}

