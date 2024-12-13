package com.vacationhomes.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.vacationhomes.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsernameAndPassword(String username, String password);
}