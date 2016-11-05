package com.codestrokes.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.codestrokes.model.Reference;

@RepositoryRestResource(collectionResourceRel="reference", path="reference")
public interface ReferenceRepository extends PagingAndSortingRepository<Reference, Long>{

}
