// package com.vacationhomes.config;

// import javax.sql.DataSource;

// import org.springframework.context.annotation.Bean;
// import org.springframework.context.annotation.Configuration;
// import org.springframework.jdbc.datasource.DriverManagerDataSource;

// @Configuration
// public class DatabaseConfig {
//     @Bean
//     public DataSource dataSource() {
//         DriverManagerDataSource dataSource = new DriverManagerDataSource();
//         dataSource.setDriverClassName("org.postgresql.Driver");
//         dataSource.setUrl("jdbc:postgresql://localhost:5432/vacation_homes");
//         dataSource.setUsername("postgres");
//         dataSource.setPassword("Yash@2000");
//         return dataSource;
//     }
// }