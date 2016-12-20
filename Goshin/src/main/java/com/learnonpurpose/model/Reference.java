package com.learnonpurpose.model;

import java.net.URI;
import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Lob;
import javax.persistence.ManyToOne;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

import org.hibernate.validator.constraints.URL;

@Entity
public class Reference {
	
	public URI getLink() {
		return link;
	}

	public void setLink(URI link) {
		this.link = link;
	}

	public Date getClick_ts() {
		return click_ts;
	}

	public void setClick_ts(Date click_ts) {
		this.click_ts = click_ts;
	}

	public Queue getBender() {
		return bender;
	}

	public void setBender(Queue bender) {
		this.bender = bender;
	}

	public Long getId() {
		return id;
	}

	@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
	Long id;
	
	//@URL
	URI link;
	
	@Temporal(TemporalType.TIMESTAMP)
	Date click_ts;
	
	@ManyToOne
	Queue bender;
	
	@ManyToOne
	Question question;
	
	String title;
	
	@Lob
	String theAbstract;

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getTheAbstract() {
		return theAbstract;
	}

	public void setTheAbstract(String theAbstract) {
		this.theAbstract = theAbstract;
	}
}
