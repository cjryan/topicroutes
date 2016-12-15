package com.learnonpurpose.model;

import java.util.Date;
import java.util.Set;

import javax.persistence.*;

@Entity
public class Tag extends ITemporal {
	
	@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
	Long id;
	
	String tag;
	
	@ManyToMany(mappedBy= "tags")
	Set<Note> notes;
}
