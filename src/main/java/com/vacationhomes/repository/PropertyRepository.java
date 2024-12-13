package com.vacationhomes.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.vacationhomes.entity.Property;

public interface PropertyRepository extends JpaRepository<Property, Long> {}