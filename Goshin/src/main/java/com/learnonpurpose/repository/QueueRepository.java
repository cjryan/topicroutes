package com.learnonpurpose.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.learnonpurpose.model.Queue;

@RepositoryRestResource(collectionResourceRel="queues", path="queues")
public interface QueueRepository extends PagingAndSortingRepository<Queue, Long>{
	

}
