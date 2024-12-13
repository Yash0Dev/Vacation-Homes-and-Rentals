package com.vacationhomes.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UiController {

    @GetMapping({"/login", "/register"})
    public String login() {
        return "login";
    }

    @GetMapping("/properties")
    public String properties() {
        return "properties";
    }

    @GetMapping("/profile")
    public String profile() {
        return "profile";
    }
}
