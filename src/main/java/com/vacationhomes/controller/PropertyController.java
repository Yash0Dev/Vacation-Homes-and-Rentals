package com.vacationhomes.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.vacationhomes.entity.Property;
import com.vacationhomes.repository.PropertyRepository;

@RestController
@RequestMapping("/api/properties")
public class PropertyController {
    @Autowired
    private PropertyRepository propertyRepository;

    @GetMapping("/list")
    public List<Property> listProperties() {
        return propertyRepository.findAll();
    }

    @PostMapping("/add")
    public ResponseEntity<String> addProperty(@RequestBody Property property) {
        propertyRepository.save(property);
        return ResponseEntity.ok("Property added successfully");
    }

    @DeleteMapping("/remove/{id}")
    public ResponseEntity<String> removeProperty(@PathVariable Long id) {
        propertyRepository.deleteById(id);
        return ResponseEntity.ok("Property removed successfully");
    }
}
