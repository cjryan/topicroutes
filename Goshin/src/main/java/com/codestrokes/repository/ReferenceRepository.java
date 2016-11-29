package com.codestrokes.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.codestrokes.model.Reference;

@RepositoryRestResource(collectionResourceRel="references", path="references")
public interface ReferenceRepository extends PagingAndSortingRepository<Reference, Long>{

}
